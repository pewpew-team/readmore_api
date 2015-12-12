from django.conf.urls import url, patterns

from books.views import BookListCreate

urlpatterns = patterns(
    '',
    url(r'^books/', BookListCreate.as_view(), name='book-list'),
)

