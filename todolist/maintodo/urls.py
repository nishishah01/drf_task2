from django.contrib import admin
from django.urls import path,include
from todolist import views
from django.contrib.auth import views as auth_views
from .views import TodoListcreateView

urlpatterns = [
   path('',views.home,name='home-page'),  #we created a homepage in the views.py so yaa
   path('todos/',TodoListcreateView.as_view(),name='todo-list-create')
   
]