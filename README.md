<b>Este README esá em inglês e português<br></b>
<b>This README is in english and portuguese</b>

# 🔐 API OTP

## Descrição

**API_OTP** é uma API desenvolvida em Python para geração e validação de códigos OTP, utilizada para autenticação em dois fatores e validação de usuários em aplicações web e mobile.  
Com esta API, é possível gerar códigos temporários, validar a entrada do usuário e reforçar a segurança de sistemas que exigem autenticação dinâmica.

## ✨ Como funciona

- Fornece endpoints para geração de códigos OTP temporários.
- Permite a validação de códigos OTP enviados por usuários.
- Pode ser integrada facilmente a aplicativos web, mobile ou outros sistemas que requeiram autenticação segura.
- Suporta configuração de tempo de expiração e customização de parâmetros de segurança.

## 🛠️ Principais Tecnologias e Bibliotecas

- 🌐 **FastAPI** ou **Flask**: framework para construção de APIs RESTful.
- 📝 **logging**: registro de logs das operações.
- 🛡️ **uvicorn** ou **gunicorn**: servidores para deploy da API.
- 📦 Outras utilidades descritas em `requirements.txt`.

*Consulte o arquivo [`requirements.txt`](./requirements.txt) para a lista completa de dependências.*

## 📁 Estrutura dos Arquivos

- `app.py`: ponto de entrada da aplicação.
- `config/`: arquivos de configuração.
- `requirements.txt`: lista de dependências do projeto.
- `utils.py`: arquivo que contém informações necessárias para realizar a conexão no banco de dados e inserir código no banco.

## ▶️ Exemplo de execução

```bash
uvicorn main:app --reload
```
Ou, caso utilize Flask:
```bash
python app.py
```

A API estará disponível para receber solicitações HTTP para geração e validação de OTP.

<br>

# 🔐 API OTP

## Description

**API_OTP** is an API developed in Python for generating and validating OTP codes, used for two-factor authentication and user validation in web and mobile applications.  
With this API, you can generate temporary codes, validate user input, and enhance the security of systems that require dynamic authentication.

## ✨ How it works

- Provides endpoints for generating temporary OTP codes.
- Allows validation of OTP codes submitted by users.
- Can be easily integrated into web, mobile, or other systems that require secure authentication.
- Supports expiration time configuration and security parameter customization.

## 🛠️ Main Technologies and Libraries

- 🌐 **FastAPI** or **Flask**: framework for building RESTful APIs.
- 📝 **logging**: operation logging.
- 🛡️ **uvicorn** or **gunicorn**: servers for API deployment.
- 📦 Other utilities described in `requirements.txt`.

*See the [`requirements.txt`](./requirements.txt) file for the complete list of dependencies.*

## 📁 File Structure

- `app.py`: application entry point.
- `config/`: configuration files.
- `requirements.txt`: project dependency list.
- `utils.py`: contains functions for database connection and code insertion.

## ▶️ Example of execution

```bash
uvicorn main:app --reload
```
Or, if using Flask:
```bash
python app.py
```

The API will be available to receive HTTP requests for OTP generation and validation.
