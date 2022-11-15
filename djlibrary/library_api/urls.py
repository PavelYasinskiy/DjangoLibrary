from django.urls import path
from .views import AuthorList, BookList

urlpatterns = [
    path('book/', BookList.as_view(), name="book_list"),
    path('author/', AuthorList.as_view(), name="author_list")

]