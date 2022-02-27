from django.shortcuts import render
from .models import Student,Class
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def hello(request):
    return HttpResponse("Hello World")
def student(request):
    # student = Student.objects.filter(Q('name'))
    student = Class.objects.filter(class_number='bscs').only('roll_number')
    
    print(student)
    



    # print(q)
    """ for x in student:
        print(x.class_number)
        print(x.roll_number) """
        
    return HttpResponse("Hello World")
    
    
    
    