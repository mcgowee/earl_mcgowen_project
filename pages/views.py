from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import include, path
from pages import views
from .models import Page
from .forms import SentimentForm

def home(request):
    return render(request, "pages/home.html")

def sentiment(response):
    if response.method == "POST":
        form = SentimentForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = SentimentForm()


    return render(response, "pages/sentiment.html", {"form": SentimentForm()})  


