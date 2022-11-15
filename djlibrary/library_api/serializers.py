from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    """Сериализация данных из модели Автор"""

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    """Сериализация данных из модели Книги"""
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

