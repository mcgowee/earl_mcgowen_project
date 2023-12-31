from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path
from pages import views

def home(request):
    return render(request=request, template_name="pages/home.html")
# Create your views here.

# Compare this snippet from pages/urls.py:
# 
# from pages import views
#


