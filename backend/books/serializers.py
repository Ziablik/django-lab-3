from rest_framework import serializers
from .models import Book, ReadingRoom, Educations, Reader, BookReader

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class ReadingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingRoom
        fields = "__all__"


class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"


class BookReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReader
        fields = "__all__"

