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
- **Aplicação estará no endpoint:** http://localhost:8000

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
- Rota: /consultar
- Método: GET
Cabeçalho:
Authorization: Bearer {token}
- Resposta Sucesso:
```bash
{
  "fact": "Dogs can understand up to 250 words and gestures."
}
```

## **Deploy na AWS**
### ** 1. Configuração do Ambiente**
Utilize o eksctl para criar um cluster Kubernetes na região desejada.


### **2. Comandos de Deploy**
Crie o cluster:

```bash
eksctl create cluster --name projeto_cloud --region us-east-2 --nodes 2
```

Configure o acesso:

```bash
aws eks --region us-east-2 update-kubeconfig --name projeto_cloud
````

Faça o deploy dos serviços:

```bash
kubectl apply -f app-deployment.yml
kubectl apply -f db-deployment.yml
```
 Acesse a aplicação:

```bash
kubectl get svc fastapi-service
```
### 3. Acesso ao Serviço
- Link:

