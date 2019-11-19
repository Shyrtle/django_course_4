from django.contrib import admin
from django.urls import path, include
from url_app import views

app_name = 'url_app'

urlpatterns = [
    path('rut/', views.relative_url_templates, name='rut'),
    path('', views.other, name='other'),
]
