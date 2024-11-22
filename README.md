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
- **Linguagem:** Python 3.10  

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
