from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def log_in(request):
    return render(request, 'log-in.html')

def create_monster(request):
    return render(request, 'create-monster.html')