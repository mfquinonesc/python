# Django

## Commands

- Install a virtual environment  `pip install virtualenv`

- Check the versin of virual env `virtualenv --version`

- Create virtual environment `virtualenv venv`

- Activate virtual environment `.\venv\Scripts\activate`

- Show and Run Commands `Select Interpreter`. This command does the same as the previous

## Installing DJango

- Install django  `pip install django`

- Check the django version `django-admin --version` or `python -m django --version`

## Create a new project

- Create a new project `django-admin startproject name`

- Create a new project in only one folder `django-admin startproject name .`

## Execute server

- Execute server `python manage.py runserver`

- Execute in defferent port  `python manage.py runserver 3000`

## Understanding the folder structure

- [Init](./djangoproject/mysite/__init__.py) 

- [Settings](./djangoproject/mysite/settings.py)  

- [Database](./djangoproject/db.sqlite3) 

- [Urls](./djangoproject/mysite/urls.py) 

- [asgi](./djangoproject/mysite/asgi.py) deploy

## Applications in Django

- Create an application `python manage.py startapp name`

## Structure of an app

- [views.py](./djangoproject/myapp/views.py) what you want to send to the client 

- [inti](./djangoproject/myapp/__init__.py)

- [migrations](./djangoproject/myapp/migrations/) has to do with the database

- [admin](./djangoproject/myapp/admin.py) 

- [apps](./djangoproject/myapp/apps.py) the settings for this app

- [models](./djangoproject/myapp/models.py) tables for the database

- [test](./djangoproject/myapp/tests.py)

## Database Models

-  Migrations `python manage.py makemigrations`

-  Migrations `python manage.py migrate`

## Django Shell

- Shell `python manage.py shell`

## Params




