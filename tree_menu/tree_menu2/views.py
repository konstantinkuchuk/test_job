from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu(request):
    return render(request, 'menu.html')

def test_tree(request):
    return render(request, 'test_tree.html')

def open(request):
    return render(request, 'open.html')
