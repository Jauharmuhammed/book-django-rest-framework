from rest_framework import serializers

from main.models import Book

class BookModelSerializers(serializers.ModelSerializer):
  class Meta:
    model= Book
    fields = '__all__' 
