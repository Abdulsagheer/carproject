from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in!!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('accounts:login')
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists!!')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists!!')
                    return redirect('accounts:register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                    auth.login(request,user)
                    messages.success(request,'You are logged in!!')
                    return redirect('accounts:dashboard')
                    user.save()
                    messages.success(request,'User registered successfully!!')
                    return redirect('accounts:login')

        
        else:
            messages.error(request,'Password does not match')
            return redirect('accounts:register')
    else:
        return render(request,'accounts/register.html')
@login_required(login_url='login')        
def dashboard(request):
    user_enquiry=Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    data={
        'enquiries':user_enquiry
    }
    return render(request,'accounts/dashboard.html',data)

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('pages:home')
    return redirect('pages:home')
