from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.TextField()
	middlename = models.TextField()
	surname = models.TextField()
	contacts = models.TextField()


class Room(models.Model):
	number = models.IntegerField()
	name = models.TextField()
	capacity = models.IntegerField()


class Reader(models.Model):
	EDUCATION_CHOICES = (
		('s', 'Начальное'),
		('m', 'Среднее'),
		('l', 'Высшее'),
	)

	number = models.IntegerField()
	firstname = models.TextField()
	middlename = models.TextField()
	surname = models.TextField()
	passport_number = models.TextField()
	birth_date = models.DateField()
	adress = models.TextField()
	t_number = models.TextField()
	education = models.CharField(max_length=1, choices=EDUCATION_CHOICES)
	hasDegree = models.BooleanField(default=False)

	date_registration = models.DateField(auto_now_add=True)
	date_out = models.DateField(default=None, null=True)

	room = models.ForeignKey(Room, on_delete=models.CASCADE)

