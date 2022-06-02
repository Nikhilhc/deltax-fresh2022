from django.shortcuts import render

# Create your views here.

def Homepage(request):
    render(request,'HomePage.html')