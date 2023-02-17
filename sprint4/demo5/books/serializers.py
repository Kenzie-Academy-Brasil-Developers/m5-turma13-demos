from rest_framework import serializers
import ipdb
from .models import Book, BookMark


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    book_owner = serializers.CharField(source="owner.username", read_only=True)

    def create(self, validated_data: dict) -> Book:
        # print("CHAMADO .create DO SERIALIZER")
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data: dict):
        # print("CHAMADO .update DO SERIALIZER")
        import ipdb

        # ipdb.set_trace()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class BookMarkSerializer(serializers.Serializer):
    chapter = serializers.IntegerField()
    note = serializers.CharField()
    book_title = serializers.CharField(source="book.title", read_only=True)
    marker = serializers.CharField(source="marker.username", read_only=True)

    def create(self, validated_data: dict) -> BookMark:
        # import ipdb

        # ipdb.set_trace()
        return BookMark.objects.create(**validated_data)
