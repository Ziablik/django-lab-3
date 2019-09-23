from rest_framework import serializers

from .models import Employee, Room, Reader


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ('id', 'firstname', 'middlename', 'surname', 'contacts')


class RoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Room
		fields = ('id', 'number', 'name', 'name')


class ReaderSerializer(serializers.ModelSerializer):
	room = RoomSerializer()

	class Meta:
		model = Reader
		fields = (
			'id', 
			'number', 
			'firstname', 
			'middlename',
			'surname', 
			'passport_number', 
			'birth_date', 
			'adress',
			't_number', 
			'education', 
			'hasDegree', 
			'date_registration',
			'date_out',
			'room'
		)


class ReaderPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reader
		fields = ( 
			'number', 
			'firstname', 
			'middlename',
			'surname', 
			'passport_number', 
			'birth_date', 
			'adress',
			't_number', 
			'education', 
			'hasDegree', 
			'room'
		)