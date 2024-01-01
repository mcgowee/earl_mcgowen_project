from django.contrib import admin
from .models import Page

admin.site.register(Page)

# Compare this snippet from pages/urls.py:
# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

    