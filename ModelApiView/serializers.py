from rest_framework import serializers
from ModelApiView.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','description','price']
        