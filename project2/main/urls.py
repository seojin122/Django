# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.index),
    path("add/", views.add),
]
