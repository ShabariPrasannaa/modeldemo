from django.shortcuts import render
from dbapp.models import Employee
# Create your views here.
def empDetails(request):
    data = Employee.objects.all()
    emp_dict = {'emp_list':data}
    return render(request,'empapp/html.html', context = emp_dict)