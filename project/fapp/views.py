from django.shortcuts import render
from .models import Employee
# Create your views here.

def display(request):
    emp=Employee.objects.all()
    template_name='fapp/display.html'
    context={'emp':emp}
    return render(request,template_name,context)