from django.contrib import admin

# Code for blog app from https://www.askpython.com/django/django-blog-app

from .models import BlogModel, CommentModel
admin.site.register(BlogModel)
admin.site.register(CommentModel)
