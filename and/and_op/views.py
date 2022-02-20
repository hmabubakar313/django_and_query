from django.shortcuts import render
from .models import Student,Class
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def hello(request):
    return HttpResponse("Hello World")
def student(request):
    student = Student.objects.filter(Q(name='ali')&Q(name='abubakar')) 

    # print(q)
    for x in student:
        print(x.name)
        print(x.father_name)
        
    return HttpResponse("Hello World")
    
    
    
    