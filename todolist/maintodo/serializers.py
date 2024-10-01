from rest_framework import serializers
from .models import todo
class TodoSerializer(serializers.ModelSerializer): #serializzer in django is respomsible for converting object to  data type which is understamdable by js and frontent framework
    class Meta:
        model=todo
        fields=['id','title','description','completed','created_at','updated_at']