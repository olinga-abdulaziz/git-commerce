from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'baseapp/home.html',{})

def manage(request):
    return render(request,'baseapp/management.html',{})

def editstock(request):
    return render(request,'baseapp/editstock.html')