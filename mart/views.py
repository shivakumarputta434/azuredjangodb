from django.shortcuts import render,HttpResponse
from .models import Emp

# Create your views here.
def home(request):
    emp=Emp.objects.get(id=1).name
    print(emp)
    return HttpResponse('welcome mart')
