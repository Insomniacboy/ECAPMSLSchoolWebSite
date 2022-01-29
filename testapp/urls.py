from django.urls import path
from . import views

urlpatterns = [
    path('testfunction', views.testfunction)
]