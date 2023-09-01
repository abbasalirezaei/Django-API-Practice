from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

class DetailTodoAPIView(generics.RetrieveAPIView):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()

class ListTodoAPIView(generics.ListAPIView):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()