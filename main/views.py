from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    data = {
        'title': 'Minima Clean & Minimal Template',
    }
    return render(request, 'main/index.html', data)


def services(request):
    return render(request, 'main/services.html')


def contacts(request):
    return HttpResponse("<h1>Shop!</h1>")