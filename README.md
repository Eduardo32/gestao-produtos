# Projeto Gestão de Produtos

Projeto gestão de produtos desenvolvido em Python com Django para o curso [Desenvolva uma aplicação com Django 2.0 e deploy no Heroku](https://www.udemy.com/django-20-heroku/) do prof. [Gregory Pacheco](https://www.udemy.com/user/gpzimpacheco/).

## Em que consiste o projeto 

Um CRUD simples onde é possivel:

* Criar uma conta com username e senha
* Consultar uma lista de produtos
* Cadastrar novos produtos
* Editar as informações de um protudo cadastrado
* Excluir produtos

## Para Instalar

Para criar uma venv executar:

```bash
python -m venv [nome_da_venv]
```

Para ativar a _venv_ executar:

```bash
[nome_da_venv]\Scripts\activate
```

Para instalar as dependências do projeto, executar:

```bash
pip install -r requirements-dev.txt
```

Criar um arquivo chamado _.env_ criar as seguintes variaves:

* SECRET_KEY (Como um secret key que você pode gerar [aqui](https://djskgen.herokuapp.com/) ou em outro site de sua preferências)
* DEBUG (Para setar o bebug como _True_ que está setado como _False_ por padrão)
* DATABASE_URL (Caso queira usar o banco de daados diferente do _SQLite3_)

Para criar as _Migrations_:

```bash
python manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

## Para Executar

Para executar o Servidor de testes do Django, execute:

```bash
python manage.py runserver
```
