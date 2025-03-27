from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm  # your custom form

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  # Make sure 'login' name is defined in urls.py
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})



from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

from django.http import HttpResponse

def email_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            print(user)
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')

    return render(request, 'login.html')




def index_view(request):
    return render(request, 'index.html') 