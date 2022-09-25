from django.shortcuts import render
from home.models import Contact

# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Contact(username=username,email=email,subject=subject,message=message)
        data.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def stories(request):
    return render(request,'stories.html')

def recipes(request):
    return render(request,'recipes.html')