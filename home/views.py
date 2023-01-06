from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# username=newuser&password=thismightbethemember
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact.html')

def loginUser(request):
    if request.method=="POST":
        #check for correct credentials
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        # print(username,password)
        if user is not None:
            login(request, user)
        # A backend authenticated the credentials
            return redirect("/")

        else:
        # No backend authenticated the credentials
            return render(request, 'index.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")