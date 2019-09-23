from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import transliterate

from .models import Reader, Room
from .serializers import ReaderSerializer, ReaderPostSerializer, RoomSerializer


class RoomList(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class ReaderList(APIView):
    def get(self, request):
        number = request.GET.get('number')
        if number:
            try:
                reader = Reader.objects.get(number=number)
            except Reader.DoesNotExist:
                raise Http404
            serializer = ReaderSerializer(reader)
        else:
            reader = Reader.objects.all()
            serializer = ReaderSerializer(reader, many=True)
        return Response(serializer.data)

    def post(self, request):
        reader = ReaderPostSerializer(data=request.data)
        if reader.is_valid():
            reader.save()
            return Response({'msg': "Success"})
        else:
            return Response({'msg': "Error"})


class ReaderDetail(APIView):
    def get_object(self, pk):
        try:
            return Reader.objects.get(id=pk)
        except Reader.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reader = self.get_object(pk)
        serializer = ReaderSerializer(reader)
        return Response(serializer.data)
