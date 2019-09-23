from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import transliterate
import datetime

from .models import Book, ReadingRoom, Educations, Reader, BookReader
from .serializers import BookSerializer, BookReaderSerializer, ReaderSerializer, ReadingRoomSerializer, EducationsSerializer


class BookList(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response({'msg': "Success"})
        else:
            return Response({'msg': "Error"})


class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


# class BookCopyList(APIView):
#     def get(self, request, pk):
#         try:
#             copy = Copy.objects.filter(book=pk)
#             serializer = CopySerializer(copy, many=True)
#             return Response(serializer.data)
#         except Copy.DoesNotExist:
#             raise Http404
#
#
# class CopyList(APIView):
#     def get(self, request):
#         cypher = request.GET.get('cypher')
#         if cypher:
#             try:
#                 copy = Copy.objects.get(cipher=cypher)
#             except Copy.DoesNotExist:
#                 raise Http404
#             serializer = CopySerializer(copy)
#         else:
#             copy = Copy.objects.all()
#             serializer = CopySerializer(copy, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         copy = CopyPostSerializer(data=request.data)
#         if copy.is_valid():
#             copy.save()
#             return Response({'msg': "Success"})
#         else:
#             return Response({'msg': "Error"})
#
#
# class CopyDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Copy.objects.get(id=pk)
#         except Copy.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         copy = self.get_object(pk)
#         serializer = CopySerializer(copy)
#         return Response(serializer.data)
#
#
#
# class RentList(APIView):
#     def get(self, request):
#         reader_number = request.GET.get('reader')
#         if reader_number:
#             try:
#                 reader = Reader.objects.get(number=reader_number)
#                 try:
#                     rent = Rent.objects.filter(reader=reader, actual_return_date=None)
#
#                 except Rent.DoesNotExist:
#                     raise Http404
#             except Reader.DoesNotExist:
#                 raise Http404
#         else:
#             rent = Rent.objects.all()
#         serializer = RentSerializer(rent, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         rent = RentPostSerializer(data=request.data)
#         if rent.is_valid():
#             rent.save()
#             return Response({'msg': "Success"})
#         else:
#             return Response({'msg': "Error"})
#
#
# class RentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Rent.objects.get(id=pk)
#         except Rent.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         rent = self.get_object(pk)
#         returner = request.GET.get('returner')
#         if returner:
#             rent.actual_return_date = datetime.datetime.now().date()
#             rent.save()
#         serializer = RentSerializer(rent)
#         return Response(serializer.data)

