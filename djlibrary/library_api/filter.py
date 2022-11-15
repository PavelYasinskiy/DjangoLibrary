import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    '''
    Фильтр модели "Книги" по количеству страниц(больше, меньше, равно),
    по названию книги и автору произведения
    '''

    class Meta:
        model = Book
        fields = {
            "name": ['exact', 'icontains'],
            "pages": ['exact', 'gt', 'lt', "gte", 'lte'],
            "author": ['exact']
        }
