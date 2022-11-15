from django.db import models

# Задание
# Создайте api публичной библиотеки электронных книг:



class Author(models.Model):
    '''
    Модель Автора книги
    :param models.Model: Наследуем стандартную модель django
    :type models.Model: class
    '''
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return self.name



class Book(models.Model):
    '''
    Модель Книги.
    :param models.Model: Наследуем стандартную модель django
    :type models.Model: class
    '''
    author = models.ForeignKey("Author", related_name='books', on_delete=models.DO_NOTHING, verbose_name="Автор")
    name = models.CharField(max_length=30, verbose_name="Название книги")
    isbn = models.IntegerField(verbose_name="Международный регистрационный номер")
    year = models.DateField(verbose_name="Год выпуска")
    pages = models.IntegerField(verbose_name="Количество страниц")
