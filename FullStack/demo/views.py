from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')
def about_view(request):
    return render(request, 'home/about.html')
def contact(request):
    # name = request.Get.get('name')
    return HttpResponse("this is the contact!")
def name(request,name):
    return render(request, 'home/home.html')
def http_resp(request):
    return HttpResponse('<h1> Welcome </h>')
def json_resp(request):
    data = {'name':'Prabhas','age':20}
    return JsonResponse(data,safe=False)