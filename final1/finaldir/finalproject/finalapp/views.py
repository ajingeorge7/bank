from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib import messages
from .forms import forma
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('finalapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('finalapp:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect('finalapp:login')
        else:
            messages.info(request, "Password not matched")
            return redirect('finalapp:register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('finalapp:new')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('finalapp:login')

    return render(request, 'login.html')

def new(request):
    return render(request, 'new.html')
def form(request):
    if request.method == 'POST':
        form = forma(request.POST)
        if form.is_valid():

            messages.success(request, 'Form submitted successfully!')


        else:
            messages.error(request, 'Form submission failed. Please check the errors.')

    else:
        form = forma()

    return render(request, 'form.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('finalapp:index')


