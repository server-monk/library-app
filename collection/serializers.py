from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'book_id',
            'book_title',
            'author',
            'description',
            'genre',
            'isbn',
            'publisher',
            'publish_year',
            'edition',
            'book_format',
            'is_available',
            'language',
            'created_at',

        ]
        # read_only_fields = 'book_id'


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'book_id',
            'book_title',
            'author',
            'description',
            'genre',
            'publisher',
            'publish_year',
            'edition',
            'book_format',
            'is_available',
            'language',

        ]


class DeletionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'book_id'
        ]