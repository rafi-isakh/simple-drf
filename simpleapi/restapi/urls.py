from django.conf.urls import url
from restapi import views

# Function based urls
# urlpatterns = [
#     url(r'^api/v1/books/$', views.book_list),
#     url(r'^api/v1/book/(?P<pk>[0-9]+)/$', views.book_detail),
#     url(r'^api/v1/book-categories/$', views.book_categories_list)
# ]

# Class based urls
urlpatterns = [
    url(r'^api/v1/books/$', views.BookList.as_view(), name=views.BookList.name),
    url(r'^api/v1/book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name=views.BookDetail.name),
    url(r'^api/v1/book-categories/$', views.BookCategoryList().as_view(), name=views.BookCategoryList.name),
    url(r'^api/v1/book-category/(?P<pk>[0-9]+)/$', views.BookCategoryDetail.as_view(), name=views.BookCategoryDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]