
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from User_management.forms import RegisterForm,Password_change_Form,Login_Form
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Home Page
def base(request):
    return render(request,'base.html')

# Thank You page After Submit
def thankyou(request):
    return render(request,'thankyou.html')

# Registration Page
def register(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You')
            return  HttpResponseRedirect('/thankyou/')
    else:
        fm=RegisterForm()
    return render(request,'register.html',{'form':fm})

# Login Page
def user_login(request):
    if not  request.user.is_authenticated:
        if request.method=='POST': 
            fm=Login_Form(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm=Login_Form()         
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change  password with old Password
def changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Password_change_Form(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Pssword Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm=Password_change_Form(user=request.user)
        return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

