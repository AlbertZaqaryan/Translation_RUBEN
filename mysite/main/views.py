from django.shortcuts import render
from .models import Person
# Create your views here.

def index(request):
    person_list = Person.objects.all()
    return render(request, 'main/index.html', context={
        'person_list':person_list
    })