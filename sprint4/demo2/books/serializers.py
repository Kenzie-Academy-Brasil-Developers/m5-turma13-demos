from rest_framework import serializers
import ipdb
from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    published_date = serializers.DateField()

    def create(self, validated_data: dict) -> Book:
        # ipdb.set_trace()
        # book = Book.objects.create(**validated_data)

        return Book.objects.create(**validated_data)
