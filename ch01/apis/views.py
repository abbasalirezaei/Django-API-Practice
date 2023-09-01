from rest_framework import generics
from rest_framework.response import Response


from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

