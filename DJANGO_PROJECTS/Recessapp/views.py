from django.shortcuts import render
from django.http import HttpResponse  
from django.template import loader

# Create your views here.
def Welcome(request):

    return render(request,'myapp.html')

def register(request):
    name=request.POST['name']
    contact=request.POST['contact']
    location=request.POST['location']
   
    return render(request,'registration.html',{"name":name,"location":location,"contact":contact}) 