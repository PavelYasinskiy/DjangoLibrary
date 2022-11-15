from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from .filter import BookFilter
from django_filters.rest_framework import DjangoFilterBackend

class BookList(ListAPIView):
    '''
    API модели "Книги" с фильтрами по количеству страниц(больше, меньше, равно),
    по названию книги и автору произведения
    :return json: Список Книг со всеми полями модели
    '''
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    filterset_fields = ['name', 'pages']



class AuthorList(ListModelMixin,CreateModelMixin , GenericAPIView):
    '''
    API модели "Автор" с  возможностью фильтрации по имени автора
    :return json: Список Авторов со всеми полями модели
    '''

    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get("name")

        if author_name:
            queryset = queryset.filter(name=author_name)

        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


