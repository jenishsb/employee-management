from django.contrib import admin
from .models import Employee, Address, Departments

# Register your models here.
class DepartmentsAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        employees_to_delete = obj.employee_set.all()
        for employee in employees_to_delete:
            employee.delete()
        obj.delete()

admin.site.register(Employee)
admin.site.register(Departments,DepartmentsAdmin)
admin.site.register(Address)