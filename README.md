# Projeto-Cloud  
**Leonardo Aragão**  

---

## **Visão Geral**  

O **Projeto-Cloud** é uma aplicação construída com **FastAPI**, com suporte para autenticação e consumo de uma API externa de fatos sobre cachorros. Ele é containerizado usando **Docker**, permitindo fácil implantação local ou em nuvem.  

### **Principais Funcionalidades**  
- Registro e login de usuários com autenticação baseada em **JWT**.  
- Consulta de fatos curiosos sobre cachorros fornecidos pela **Dog API**.  

---

## **Tecnologias Utilizadas**  
- **Framework Backend:** FastAPI  
- **Banco de Dados:** MySQL  
- **Autenticação:** JWT  
- **ORM:** SQLAlchemy  
- **Containerização:** Docker e Docker Compose  

---

## **Pré-requisitos**  

Certifique-se de ter as seguintes ferramentas instaladas no sistema:  
1. **Docker:** Para gerenciar containers.  
2. **Docker Compose:** Para orquestrar múltiplos serviços.  

---

## **Instruções de Instalação e Uso Local**  

### **1. Clonando o Repositório**  
```bash
git clone <URL-do-repositorio>
cd <nome-do-repositorio>
```

### **2. Subindo os Containers**
Execute o seguinte comando para iniciar os serviços:

```bash
docker-compose up
```
- **Documentação Interativa da API:** http://localhost:8000

---
  
## **Descrição dos Endpoints**
### **1. Registro de Usuário**
- Rota: /register
- Método: POST
- Parâmetros:
```bash
{
  "nome": "string",
  "email": "string",
  "senha": "string"
}
```
- Resposta Sucesso:
```bash
{
  "token": "jwt_token"
}
```
### **2. Login de Usuário**
- Rota: /login
- Método: POST
- Parâmetros:
```bash
{
  "email": "string",
  "senha": "string"
}
```
Resposta Sucesso:
```bash
{
  "token": "jwt_token"
}
```
### **3. Consulta de Fatos Sobre Cachorros**
Rota: /consultar
Método: GET
Cabeçalho:
css
Copiar código
Authorization: Bearer {token}
Resposta Sucesso:
json
Copiar código
{
  "fact": "Dogs can understand up to 250 words and gestures."
}
Exemplo de Fluxo com cURL
Registro de Usuário
bash
Copiar código
curl -X POST http://localhost:8000/register \
     -H "Content-Type: application/json" \
     -d '{"nome": "Leonardo", "email": "leonardo@email.com", "senha": "senha123"}'
Login
bash
Copiar código
curl -X POST http://localhost:8000/login \
     -H "Content-Type: application/json" \
     -d '{"email": "leonardo@email.com", "senha": "senha123"}'
Consulta
bash
Copiar código
curl -X GET http://localhost:8000/consultar \
     -H "Authorization: Bearer <jwt_token>"
Deploy na AWS
1. Configuração do Ambiente
Utilize o eksctl para criar um cluster Kubernetes na região desejada.
Certifique-se de ter acesso configurado ao AWS CLI com permissões suficientes.
2. Comandos de Deploy
Crie o cluster:

bash
Copiar código
eksctl create cluster --name projeto_cloud --region us-east-2 --nodes 2
Configure o acesso:

bash
Copiar código
aws eks --region us-east-2 update-kubeconfig --name projeto_cloud
Faça o deploy dos serviços:

bash
Copiar código
kubectl apply -f kubernetes/app-deployment.yml
kubectl apply -f kubernetes/db-deployment.yml
Exponha a aplicação:

bash
Copiar código
kubectl expose deployment app --type=LoadBalancer --name=app-service
3. Acesso ao Serviço
Após a criação do Load Balancer, obtenha o IP público para acessar a aplicação diretamente.

Diferenciais do Projeto
Autenticação segura: Tokens JWT para proteger os endpoints.
Escalabilidade: Suporte para Kubernetes e fácil integração com a AWS.
Usabilidade: Documentação clara e endpoints intuitivos.

