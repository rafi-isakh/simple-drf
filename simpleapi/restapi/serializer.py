from rest_framework import serializers
from restapi.models import Book

class BookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    publish_date = serializers.DateTimeField()
    book_category = serializers.CharField(max_length=200)
    read = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.book_category = validated_data.get('book_category', instance.book_category)
        instance.read = validated_data.get('read', instance.read)

        instance.save()
        return instance