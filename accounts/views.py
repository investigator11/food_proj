from django.shortcuts import render

def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
    return render(request,'login.html')

# Create your views here.
