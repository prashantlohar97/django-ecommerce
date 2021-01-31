from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
from products.models import Product

def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
            messages.info(request,'logged in.')
        else:
            messages.info(request,'invalid cred..')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        # description = request.POST['description']
        # mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register') 
            else:
                user = User.objects.create_user(first_name=first_name,username=username,email=email,password=password1)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not match...')
            return redirect('register') 

        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):
	query = request.GET['query']
	custm = Product.objects.filter(name__icontains=query)
	return render(request,'search.html',{'custm':custm})