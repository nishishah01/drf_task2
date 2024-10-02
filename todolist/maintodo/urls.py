
from django.urls import path
from .views import *


urlpatterns = [
   
   path('<int:pk>/',MoreTodo.as_view()),
   path('',TodoListcreateView.as_view()),
   path('create',createTodo.as_view()),
   path('delete/<int:pk>',DeleteTodo.as_view()),
]