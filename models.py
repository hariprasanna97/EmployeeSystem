from django.db import models
from django.utils import timezone
from _datetime import datetime


class EmployeeInfo(models.Model):
    first_name = models.CharField(max_length=200, default='firstname')
    last_name = models.CharField(max_length=200, default='lastname')
    email = models.EmailField(blank=True, null= True)
    # date_of_birth = models.DateTimeField()
    previous_employer = models.CharField(max_length=200, default='asd')

    def __str__(self):
        return self.first_name + '' + self.last_name + '' + str(self.pk)


class Choice(models.Model):
    employee = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return EmployeeInfo.first_name
