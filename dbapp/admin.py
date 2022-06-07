from django.contrib import admin
from dbapp.models import employee 
# Register your models here.
class EmployeeAdmin(admin,ModelAdmin):
    emp_details = ['empno', 'empName']

admin.site.register(employee, EmployeeAdmin)
