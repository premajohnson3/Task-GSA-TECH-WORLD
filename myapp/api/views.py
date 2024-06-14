from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User, Task
import googlemaps

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = make_password(request.POST['password'])
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        User.objects.create(username=username, email=email, mobile_number=mobile_number, password=password, address=address, latitude=latitude, longitude=longitude)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'dashboard.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_time = request.POST['date_time']
        assigned_to = User.objects.get(id=request.POST['assigned_to'])
        Task.objects.create(name=name, date_time=date_time, assigned_to=assigned_to)
        return redirect('dashboard')
    users = User.objects.all()
    return render(request, 'add_task.html', {'users': users})

def logout(request):
    auth_logout(request)
    return redirect('login')


