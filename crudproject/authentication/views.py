from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from .forms import BooksRegistration
from .models import Books

#Home view Function
def home(request):
    return render(request,'authentication/home.html')

# Signup View Function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!')
            fm.save()
    else:        
     fm = SignUpForm()
    return render(request,"signup.html",{'form':fm})
    
#login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!')
                    return HttpResponseRedirect('/addandshow/')
        else:
            fm = AuthenticationForm()
        return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/addandshow/')  



#Logout View Function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')




def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data =request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request ,fm.user )
                messages.success(request, 'Password Changed Successfully!!')
                return HttpResponseRedirect('/addandshow/')
        else:   
            fm =PasswordChangeForm(user=request.user)
        return render(request,'authentication/changepass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/signup/')


#This function will Add new book and Show all books
def add_show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = BooksRegistration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['book_name']
                em = fm.cleaned_data['author']
                am = fm.cleaned_data['published_on']
                sm = fm.cleaned_data['category']
                pn = fm.cleaned_data['price']
                
                reg = Books(book_name = nm, author=em,published_on =am,category=sm,price=pn)
                reg.save()
                #fm = BooksRegistration()
                return HttpResponseRedirect("/login/")
        else:
            fm = BooksRegistration()
        led = Books.objects.all()
            


        return render(request, 'authentication/addandshow.html',{'form':fm ,'ld':led , 'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



#This function will delete books
def delete_data(request , id):
    if request.method == 'POST':
        pi = Books.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow/')


#This Function will Update or Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = Books.objects.get(pk=id)
        fm = BooksRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Books.objects.get(pk=id)
        fm = BooksRegistration(instance=pi)
    return render(request, 'authentication/update.html' , {'form':fm})








