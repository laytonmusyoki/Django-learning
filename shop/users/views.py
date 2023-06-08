from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import Register
from .models import Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        user=Register
        if request.method=='POST':
            user=Register(request.POST)
            if user.is_valid():
                user.save()
                messages.success(request, f"Account created successfully")
                return redirect('login')
            
        
        context={
            "user":user
        }
        return render(request, 'register.html',context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home')
            else:
                messages.warning(request, 'Wrong credentials')
                return render(request, 'login.html')
        return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    shoes=Products.objects.all()
    context={
        "shoes":shoes
    }
    return render(request, 'home.html',context)


def logoutuser(request):
    logout(request)
    messages.warning(request, 'You have been logged out')
    return redirect('login')