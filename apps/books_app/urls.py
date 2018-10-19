from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books$', views.addBook, name='addBook'),
    url(r'^authors$', views.addAuthor, name='addAuthor'),
]