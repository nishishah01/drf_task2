from django.shortcuts import render

# Create your views here.


from .models import *
from .serializers import *
from rest_framework import generics

class TodoListcreateView(generics.ListAPIView):  #this is to read 
     queryset=todo.objects.all()  ##models ke liye
     serializer_class = TodoSerializer
        
        
class MoreTodo(generics.RetrieveUpdateAPIView):   #this is to update
    queryset=todo.objects.all() ##models ke lilye
    serializer_class=TodoSerializer
    
class createTodo(generics.CreateAPIView):
    queryset=todo.objects.all() ##models
    serializer_class=TodoSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset=todo.objects.all() ##models
    serializer_class=TodoSerializer