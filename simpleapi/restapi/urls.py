from django.conf.urls import url
from restapi import views

urlpatterns = [
    url(r'^api/v1/books/$', views.book_list),
    url(r'^api/v1/books/(?P<pk>[0-9]+)/$', views.book_detail)
]