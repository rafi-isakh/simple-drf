from rest_framework import serializers
from restapi.models import Book
from restapi.models import BookCategory

# Using serializer

# class BookSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     publish_date = serializers.DateTimeField()
#     book_category = serializers.CharField(max_length=200)
#     read = serializers.BooleanField(required=False)

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.publish_date = validated_data.get('publish_date', instance.publish_date)
#         instance.book_category = validated_data.get('book_category', instance.book_category)
#         instance.read = validated_data.get('read', instance.read)

#         instance.save()
#         return instance

# Using model serializer
class BookCategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail'
    )
    class Meta:
        model = BookCategory
        fields = (
            'url',
            'pk',
            'name',
            'books'
        )

class BookSerializer(serializers.ModelSerializer):
    book_category = serializers.SlugRelatedField(queryset=BookCategory.objects.all(), slug_field='name')
    class Meta:
        model = Book
        fields = (
            'url',
            'title',
            'publish_date',
            'book_category',
            'read'
        )
