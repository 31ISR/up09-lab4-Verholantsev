from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.communities, name="communities")
    path('<slug:slug>', views.community_page, name="community" )
]