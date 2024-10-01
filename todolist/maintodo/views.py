from django.shortcuts import render

# Create your views here.
from rest_framework import Response
from rest_framework.views import APIView
from .models import todo
from .serializers import TodoSerializer

class TodoListcreateView(APIView):
    def get(self, request):  ##get-to display
        todos=todo.objects.all()  ##models ke liye
        serializer = TodoSerializer(todos ,many=True)
        return Response(serializer.data)
    
    def post(self, request): ##opost-create 
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)