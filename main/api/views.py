from rest_framework import viewsets

from .serializer import BookModelSerializers
from main.models import Book

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookModelSerializers