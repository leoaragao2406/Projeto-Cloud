from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import hashlib
import jwt
import requests
import json
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

load_dotenv()
# Rodar fastapi: uvicorn main:app --reload 

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
SECRET_KEY = "ugauga"
bearer_scheme = HTTPBearer()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)

Base.metadata.create_all(bind=engine)
app = FastAPI(title='Projeto Cloud - Fatos Interessantes Sobre Cachorros', docs_url='/')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cria_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return token

def verifica_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token passou do tempo de validade")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token inválido")

@app.post('/register', tags=['Cadastro'])
def registro(nome: str, email: str, senha: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ja existe")
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    new_user = User(nome=nome, email=email, senha=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token_data = {'user_id': new_user.id, 'email': new_user.email}
    token = cria_token(token_data)
    return {'token': token}

@app.post('/login', tags=['Login'])
def login(email: str, senha: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados inválidos")
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    if user.senha != hashed_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados inválidos")
    token_data = {'user_id': user.id, 'email': user.email}
    token = cria_token(token_data)
    return {'token': token}

@app.get("/consultar", tags=['Consulta Fatos'])
def consultar_fatos(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    
    verifica_token(token)

    url = f"http://dog-api.kinduff.com/api/facts"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)['facts'][0]
        return data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao fazer requisição para a API")