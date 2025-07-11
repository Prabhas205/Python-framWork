from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')
def about_view(request):
    return render(request, 'home/about.html')
