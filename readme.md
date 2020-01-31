# Commands to start a django startproject

- pip3 install django
- django-admin startproject <project_name>
- python3 manage.py startapp <app_name>
- as soon as you create an app, set this in the settings.py at the INSTALLED_APPS.
- when created a class in models you need to create a migration file the command is:
  - python3 manage.py makemigrations
- then to apply changes to the table "if" the class changed or not:
  - python3 manage.py migrate
