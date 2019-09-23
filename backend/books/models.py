from django.db import models


# Create your models here.

class ReadingRoom(models.Model):
    room_name = models.CharField('Название', max_length=50)
    people_count = models.IntegerField('Вместимость')

    class Meta:
        verbose_name = 'Читательский зал'
        verbose_name_plural = 'Читательские залы'

    def __str__(self):
        return self.room_name


class Book(models.Model):
    room = models.ForeignKey(
        ReadingRoom,
        verbose_name='Читательский зал',
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField('Название книги', max_length=50)
    authors = models.CharField('Авторы', max_length=255)
    publishing = models.CharField('Издательство', max_length=100)
    section = models.TextField('Раздел')
    code = models.CharField('Шифр книги', max_length=100)
    active = models.BooleanField('Наличие книги', default=True)
    registration_date = models.DateField('Дата издательства', null=True)
    deleted = models.BooleanField('Удалена', default=False)
    deleted_at = models.DateField('Дата удаления', null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Educations(models.Model):
    name = models.CharField('Образование', max_length=100)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def __str__(self):
        return self.name


class Reader(models.Model):
    library_ticket = models.IntegerField('Номер читательского билета')
    room = models.ForeignKey(
        ReadingRoom,
        verbose_name='Читательский зал',
        on_delete=models.SET_NULL,
        null=True
    )
    surname = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Отчество', max_length=50)
    passport_number = models.IntegerField('Номер пасспорта')
    birthday = models.DateField('День рождение')
    addr = models.CharField('Адрес', max_length=100)
    phone = models.CharField('Номер телефона', max_length=50)
    education = models.ForeignKey(
        Educations,
        verbose_name='Образование',
        on_delete=models.SET_NULL,
        null=True
    )
    science_degree = models.BooleanField('Ученая степень')
    active = models.BooleanField('Записан читатель или нет', default=True)
    deleted_at = models.DateField('Дата удаления', null=True)
    registration_date = models.DateField('Дата регистрации', null=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.surname + ' ' + self.first_name + ' ' + self.second_name


class BookReader(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        on_delete=models.CASCADE,
        null=True
    )
    reader = models.ForeignKey(
        Reader,
        verbose_name='Читатель',
        on_delete=models.CASCADE,
        null=True
    )
    start_date = models.DateField('Дата выдачи книги')
    finish_date = models.DateField('Дата возврата книги', blank=True, null=True)

    class Meta:
        verbose_name = 'Информация о закрепленной книги'
        verbose_name_plural = 'Информация о закрепленных книгах'

    def __str__(self):
        return self.reader.__str__() + ': ' + self.book.name
