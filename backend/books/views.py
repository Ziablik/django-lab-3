import datetime

from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Book, Reader, BookReader, ReadingRoom, Educations
from .serializers import BookSerializer, ReaderSerializer, ReadingRoomSerializer, EducationsSerializer, \
    BookReaderSerializer


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

    def delete(self, request):
        book = get_object_or_404(Book, id=request.data['id'])
        book.delete()
        return Response({'msg': "Success"})


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


class WorkTable(APIView):
    def get(self, request):
        data = []
        today = datetime.date.today()
        bookreaders = BookReader.objects.filter(finish_date=None)
        bookreaders_month = []
        bookreaders_enought = []

        for bookreader in bookreaders:
            if (today - bookreader.start_date).days >= 30:
                bookreaders_month.append({
                    "book": {
                        'name': bookreader.book.name,
                    },
                    "reader": {
                        'fio': bookreader.reader.surname + " " + bookreader.reader.second_name + " " + bookreader.reader.first_name,
                        'library_ticket': bookreader.reader.library_ticket,
                    },
                    "start_date": bookreader.start_date,
                    "finish_date": bookreader.finish_date,
                })

        for bookreader in bookreaders:
            if Book.objects.filter(name=bookreader.book.name).count() < 3:
                bookreaders_enought.append({
                    "book": {
                        'name': bookreader.book.name,
                    },
                    "reader": {
                        'fio': bookreader.reader.surname + " " + bookreader.reader.second_name + " " + bookreader.reader.first_name,
                        'library_ticket': bookreader.reader.library_ticket,
                    },
                    "start_date": bookreader.start_date,
                    "finish_date": bookreader.finish_date,
                })
        readers = Reader.objects.filter(birthday__gte='1999-01-01')
        readers_json = []

        for reader in readers:
            readers_json.append({
                'fio': reader.surname + " " + reader.second_name + " " + reader.first_name,
                "library_ticket": reader.library_ticket,
                "birthday": reader.birthday,
                "registration_date": reader.registration_date
            })

        data_dgrm = [0, 0, 0, 0]
        count = 0
        for reader in Reader.objects.all():
            if reader.science_degree:
                data_dgrm[3] += 1
            elif reader.education.name == 'Среднее специальное':
                data_dgrm[0] += 1
            elif reader.education.name == 'Среднее образование':
                data_dgrm[1] += 1
            elif reader.education.name == 'Высшее образование':
                data_dgrm[2] += 1
            count += 1

        data_dgrm[0] = {
            'label': 'Среднее специальное',
            'value': data_dgrm[0] / count * 100,
            'color': 'red',
        }
        data_dgrm[1] = {
            'label': 'Срднее образование',
            'value': data_dgrm[1] / count * 100,
            'color': 'green',
        }
        data_dgrm[2] = {
            'label': 'Высшее образование',
            'value': data_dgrm[2] / count * 100,
            'color': 'blue',
        }
        data_dgrm[3] = {
            'label': 'Научная степень',
            'value': data_dgrm[3] / count * 100,
            'color': 'purple',
        }

        data.append({
            'bookreaders_month': bookreaders_month,
            'bookreaders_enought': bookreaders_enought,
            'readers_json': readers_json,
            'data_dgrm': data_dgrm,
        })

        return JsonResponse(data, safe=False)


class ReaderList(APIView):
    def get(self, request):
        reader = Reader.objects.all()
        serializer = ReaderSerializer(reader, many=True)
        return Response(serializer.data)

    def post(self, request):
        reader = ReaderSerializer(data=request.data)
        if reader.is_valid():
            reader.registration_date = datetime.date.today()
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


class ReadingRoomList(APIView):
    def get(self, request):
        reading_room = ReadingRoom.objects.all()
        serializer = ReadingRoomSerializer(reading_room, many=True)
        return Response(serializer.data)


class EducationList(APIView):
    def get(self, request):
        education = Educations.objects.all()
        serializer = EducationsSerializer(education, many=True)
        return Response(serializer.data)


class BookReaderAdd(APIView):
    def post(self, request):
        bookreader = BookReaderSerializer(data=request.data)
        if bookreader.is_valid():
            book = Book.objects.get(id=request.data['book'])
            book.active = False
            book.save()
            bookreader.save()
            return Response({'msg': "Success"})
        else:
            print('error')
            return Response({'msg': "Error"})


class BookReturn(APIView):
    def post(self, request):
        book = get_object_or_404(Book, id=request.data['id'])
        book.active = True
        book.save()
        book_reader = get_object_or_404(BookReader, book=book, finish_date=None)
        book_reader.finish_date = datetime.date.today()
        book_reader.save()
        return Response({'msg': 'Success'})