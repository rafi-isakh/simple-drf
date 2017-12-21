from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, generics
from restapi.models import Book
from restapi.models import BookCategory
from restapi.serializer import BookSerializer, BookCategorySerializer

# Function based view

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         book_serializer = BookSerializer(books, many=True)
#         return Response(book_serializer.data)

#     elif request.method == 'POST':
#         book_serializer = BookSerializer(data=request.data)
        
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return Response(book_serializer.data, status=status.HTTP_201_CREATED)

#         return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         book_serializer = BookSerializer(book)
#         return Response(book_serializer.data)

#     elif request.method == 'PUT':
#         book_serializer = BookSerializer(book, data=request.data)

#         if book_serializer.is_valid():
#             book_serializer.save()
#             return Response(book_serializer.data)

#         return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def book_categories_list(request):
#     if request.method == 'GET':
#         book_categories = BookCategory.objects.all()
#         book_serializer = BookCategorySerializer(book_categories, many=True)
#         return Response(book_serializer.data)

#     elif request.method == 'POST':
#         book_serializer = BookCategorySerializer(data=request.data)
        
#         if book_serializer.is_valid():
#             book_serializer.save()
#             return Response(book_serializer.data, status=status.HTTP_201_CREATED)

#         return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class based views
class BookCategoryList(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-list'

class BookCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    name = 'bookcategory-detail'

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-list'

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    name = 'book-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
        'book-categories': reverse(BookCategoryList.name, request=request),
        'books': reverse(BookList.name, request=request)
    })