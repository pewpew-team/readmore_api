from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Book.all_to_user(self.request.user)
        else:
            return []


class BookRetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer
