from django.shortcuts import render
from pathlib import Path

def index(request):
    return render(request, 'index.html')
