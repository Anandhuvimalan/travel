from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TravelPlace,TeamMembers
from django.contrib.auth.models import User
from django.contrib import messages,auth

def home(request):
    place_data=TravelPlace.objects.all()
    team_members=TeamMembers.objects.all()
    context={
        'places':place_data,
        'teams':team_members,
    }
    return render(request,'index.html',context)

def login(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'ivalid username or password')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                print('user created successfully')
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')  
    return render(request,'register.html')
