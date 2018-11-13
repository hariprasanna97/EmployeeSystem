from django.contrib import admin

# Register your models here.
from .models import EmployeeInfo, Choice

admin.site.register(EmployeeInfo)
admin.site.register(Choice)
