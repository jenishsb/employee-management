from django.contrib import admin
from .models import Employee, Department, Address, All_Departments

# Register your models here.
admin.site.register(Employee)
admin.site.register(All_Departments)
admin.site.register(Department)
admin.site.register(Address)