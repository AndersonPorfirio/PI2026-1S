# SCR - Sistema de Cadastro de Reparos 🛠️

[cite_start]Sistema desenvolvido para o Projeto Integrador da UNIVESP, focado no gerenciamento de manutenções em oficinas de eletrônicos[cite: 9, 74, 149].

## 🚀 Tecnologias Utilizadas
* [cite_start]**Backend:** Python 3.14 + Django 6.0 [cite: 23, 76, 172]
* [cite_start]**Banco de Dados:** MySQL [cite: 23, 77, 110]
* [cite_start]**API:** Django REST Framework [cite: 176]
* [cite_start]**Frontend:** HTML5 e CSS3 (Custom Dark Theme) [cite: 78, 85, 86]

## 📋 Funcionalidades
* [cite_start]Autenticação de usuários (Técnicos e Administradores) [cite: 107, 221]
* [cite_start]Dashboard com cards de reparos efetuados [cite: 219, 230, 242]
* [cite_start]Cadastro de novos reparos e equipamentos [cite: 82, 154, 224]
* API Pública para consulta de histórico: `/api/v1/consultar/`
* [cite_start]Área de gestão para remoção de registros e usuários [cite: 223]

## 🛠️ Como rodar o projeto
1. [cite_start]Clone o repositório: `git clone https://github.com/AndersonPorfirio/PI2026-1S` [cite: 251]
2. [cite_start]Crie a venv: `python -m venv venv` [cite: 174]
3. Instale as dependências: `pip install -r requirements.txt`
4. [cite_start]Configure seu MySQL no arquivo `settings.py` [cite: 44, 193]
5. [cite_start]Rode as migrações: `python manage.py migrate` [cite: 208, 210]
6. [cite_start]Inicie o servidor: `python manage.py runserver` [cite: 183]