from django.contrib import admin
from .models import Employee, Room

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['surname', 'firstname', 'contacts']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'capacity']


admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)