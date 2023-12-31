from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="detail"),
    path("<int:question_id>/", views.detail, name="title"),
]