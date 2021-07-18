from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
#from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm,SignUpForm  #importing files created forms.py

from django.contrib import messages

# Create your views here.

def registerPage(request):
    form=RegisterForm()

    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Sucessfully!!")
        else:
            messages.success(request,"Sorry Account not created.")

    context={'form':form}
    return render(request,"usersReg/Register.html",context)

def SignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            return render(request,"usersReg/login.html")
        else:
            messages.success(request,"Invalid Credentials")  
            return render(request,"usersReg/SignUp.html")
    else:
           
        return render(request,"usersReg/SignUp.html")       