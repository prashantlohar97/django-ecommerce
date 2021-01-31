# django-ecommerce

Requirements
Python (3.5, 3.6, 3.7, 3.8, 3.9)
Django (2.2, 3.0, 3.1)


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


product API: 
http://127.0.0.1:8000/v1/product-list/
http://127.0.0.1:8000/v1/product-detail/4/
http://127.0.0.1:8000/v1/product-create/
http://127.0.0.1:8000/v1/product-update/4/ (only superuser can perform this certain operation)
http://127.0.0.1:8000/v1/product-delete/4/ (only superuser can perform this certain operation)


category API: In category only one api's becase it's similar to prodcuts crud operaion
http://127.0.0.1:8000/v1/category-list/


