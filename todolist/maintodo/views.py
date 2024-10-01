from django.shortcuts import render

# Create your views here.
from rest_framework import Response
from rest_framework.views import APIView
from .models import todo
from .serializers import TodoSerializer
from rest_framework import generics

class TodoListcreateView(generics.ListAPIView):  #this is to read 
    def get(self, request):  ##get-to display
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