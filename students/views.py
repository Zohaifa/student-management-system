from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Students
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'students/index.html', {'Students': Students.objects.all() })

def view_students(request, id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))