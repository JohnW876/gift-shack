from django.contrib import admin
from django.urls import path
from .views import *

# Code for blog app from https://www.askpython.com/django/django-blog-app

urlpatterns = [
    path('blogs/', BlogListView, name='blogs'),
    path('blog/<int:_id>', BlogDetailView, name='blog'),
]
