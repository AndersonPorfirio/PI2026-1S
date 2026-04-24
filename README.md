# SCR - Sistema de Cadastro de Reparos 🛠️

Sistema desenvolvido para o Projeto Integrador da UNIVESP, focado no gerenciamento de manutenções em oficinas de eletrônicos.

## 🚀 Tecnologias Utilizadas
 **Backend:** Python 3.14 + Django 6.0
 **Banco de Dados:** MySQL
 **API:** Django REST Framework
 **Frontend:** HTML5 e CSS3 (Custom Dark Theme)

## 📋 Funcionalidades
* Autenticação de usuários (Técnicos e Administradores)
* Dashboard com cards de reparos efetuados
* Cadastro de novos reparos e equipamentos
* API Pública para consulta de histórico: `/api/v1/consultar/`
* Área de gestão para remoção de registros e usuários

## 🛠️ Como rodar o projeto
1. Clone o repositório: `git clone https://github.com/AndersonPorfirio/PI2026-1S`
2. Crie a venv: `python -m venv venv`
3. Instale as dependências: `pip install -r requirements.txt`
4. Configure seu MySQL no arquivo `settings.py`
5. Rode as migrações: `python manage.py migrate`
6. Inicie o servidor: `python manage.py runserver`
