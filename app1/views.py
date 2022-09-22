from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , UserChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash

# Create your views here.


def home(request):
    

    context={'home':'active'}
    return render (request,'home.html',context)

def About(requerst):
    username='atiar'
    user=User.objects.get(username=username)
    about_me=AboutContent.objects.get(username=user)
    sk=Skill.objects.filter(username=user)
    ct=Countup.objects.filter(username=user)
    testi=Testimonial.objects.filter(username=user)
    
    
    context={'about':'active','about':about_me,'skill':sk, 'count':ct,'ts':testi}
    return render (requerst,'about.html',context)


def Portfolio(requerst):

    context={'portfolio':'active'}
    return render (requerst,'portfolio.html',context)


def Resume(requerst):
    username='atiar'
    user=User.objects.get(username=username)
    edu=Education.objects.filter(username=user)
    summ=Summary.objects.get(username=user)
    profesionalEx=ProfesionalExperience.objects.filter(username=user)
     
    context={'resume':'active','education':edu,'summary':summ,'pro':profesionalEx}
    return render (requerst,'resume.html',context)

def Service(request):
    username='atiar'
    user=User.objects.get(username=username)
    ser=ServicePart.objects.filter(username=user)
    
    
    

    context={'service':'active','service':ser}

    return render(request,'services.html',context)


def Contact(request):
    username='atiar'
    user=User.objects.get(username=username)
    maps=Map.objects.get(username=user)

    context={'contact':'active','maps':maps}
    return render(request,'contact.html',context)

def Registration(request):
    if request.method == 'POST':

        fm=Register(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created !')
            fm.save()
            fm=Register()
    else:
        fm=Register()
    contex= {'form':fm}
    
    return render(request,'register.html',contex)

def Login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            messages.success(request,'Login Successfull !!')
            uname=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=uname , password=password)
            if user is not None:
                login(request,user)
                return redirect('/profile')
    else:
        fm=AuthenticationForm()
    context={'form':fm}
    return render(request,'loging.html',context)


def Profile(request):
    if request.user.is_authenticated:
      if request.method =='POST':
            if request.user.is_superuser == True :
               fm=UseradminchageForm(request.POST , instance=request.user)
               messages.success(request,'Update succesfull !!')
            else:
               fm=Userchage(request.POST , instance=request.user)
               if  fm.is_valid():
                  messages.success(request,'Update succesfull !!')
                  fm.save()
      else:
        if request.user.is_superuser == True :
            fm=UseradminchageForm(instance=request.user)
        else:    
         fm=Userchage( instance=request.user)
         

      return render(request,'profile.html',{'name':request.user , 'form':fm})
    
    else:
       return redirect('/login')


def Logout(request):
    logout(request)
    messages.success(request,'Logout Successfull!!')
    return redirect('/login')
def Changepassword(request):
  if request.user.is_authenticated: 
     if request.method == 'POST':
        fm= ChangepassForm(user=request.user , data=request.POST)
        if fm.is_valid():
           messages.success(request,'Password change succesfull !!')
           fm.save()
           update_session_auth_hash(request,fm.user)
        return redirect('/profile')
     else:
        fm= ChangepassForm(user=request.user)
  else: 
      return redirect('/login')     
  context={'form':fm}
  return render(request,'changepass.html',context)


