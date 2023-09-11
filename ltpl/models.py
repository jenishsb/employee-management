from __future__ import unicode_literals
from django.db import models

# added manually
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
    username = models.CharField(max_length=12, primary_key=True)
    phno = models.IntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "emp"

    def __str__(self):
        return f'{self.username}'

# All Departments Model
class All_Departments(models.Model):
    department_name = models.CharField(max_length=50)

    class Meta:
        db_table = "all_departments"

    def __str__(self):
        return self.department_name

# Department Model
class Department(models.Model):
    name = models.ForeignKey(All_Departments, on_delete=models.CASCADE, related_name='departments')
    employees = models.ManyToManyField(Employee, related_name='departments')

    class Meta:
        db_table = "department"

    def __str__(self):
        return str(self.name)


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