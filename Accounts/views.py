from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # if request.method=='POST':
    #     username = request.POST['USERNAME']
    #     password = request.POST['password']
    #     user = auth.authenticate(username=username,password=password)

    #     if user is not None:
    #         auth.login(request,user)
    #         messages.info(request, 'logged in')
    #         return HttpResponse("User logged in")
    #     else:
    #         messages.info(request,'invalid credentiall')
    #         return redirect('home')

    # else:
        # return render(request,'login.html')
    return render(request,'login.html')

def Stafflogin(request):
    if request.method=='POST':
        username = request.POST['USERNAME']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            staffuser = User.objects.get(username=username)
            if staffuser.is_staff == True:
                auth.login(request,user)
                messages.info(request, 'logged in')
                return redirect("Handlereception")
            else:
                messages.info(request,'You are not staff.')
                return redirect('home')
        else:
            messages.info(request,'invalid credentiall')
            return redirect('home')

    else:
        return render(request,'login.html')

def Customerlogin(request):
    if request.method=='POST':
        username = request.POST['USERNAME']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            customeruser = User.objects.get(username=username)
            if customeruser.is_staff  == False:
                auth.login(request,user)
                messages.info(request, 'logged in')
                return redirect("Handlecustomer")
            else:
                messages.info(request,'You are not customer.')
                return redirect('home')
        else:
            messages.info(request,'invalid credentiall')
            return redirect('home')

    else:
        return render(request,'login.html')

def signup(request):
    user = User.objects.create_user('aman12', 'aman@gmail.com', '1234')
    user.save()
    return redirect('home')

def Handlereception(request):
    return render(request, 'Reception.html')

def Handlecustomer(request):
    return render(request, 'customer.html')

def handleLogout(request):
    auth.logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
    
