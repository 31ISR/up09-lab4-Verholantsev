from django.contrib import admin
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities, name="list"),
    path('<slug:slug>', views.community_page, name="page" )
]