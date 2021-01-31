# django-ecommerce

Requirements
Python (3.5, 3.6, 3.7, 3.8, 3.9)
Django (2.2, 3.0, 3.1)
We highly recommend and only officially support the latest patch release of each Python and Django series.

Installation
Install using pip...

pip install djangorestframework
Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Example
Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
