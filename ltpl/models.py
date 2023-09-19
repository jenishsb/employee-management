from __future__ import unicode_literals
from django.db import models


# Departments Model
class Departments(models.Model):
    department_name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        db_table = "departments"

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    GENDER_CHOICES = (
        ('Select', '--- Select Gender ---'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    gender = models.CharField(choices=GENDER_CHOICES, default='Select', max_length=12)
    phno = models.IntegerField()
    email = models.EmailField(max_length=30)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    username = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "emp"

    def __str__(self):
        return f'{self.username}'


# Address Model
class Address(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    class Meta:
        db_table = "address"

    def __str__(self):
        return f'Address of {self.employee.username}'