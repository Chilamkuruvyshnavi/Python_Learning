from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import LoginForm, RegistrationForm
from .models import UserRegistration

@require_http_methods(["GET", "POST"])
def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            try:
                # Create user account
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                
                # Create user registration record
                UserRegistration.objects.create(
                    user=user,
                    email=email
                )
                
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('success')
            
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return render(request, 'users/register.html', {'form': form})
        
        else:
            # Form has errors - they will be displayed in template
            pass
    
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


def success(request):
    """Display success page after registration"""
    return render(request, 'users/success.html')


@require_http_methods(["GET", "POST"])
def login_view(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """Log the user out and redirect to home"""
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def user_list(request):
    """List all registered users from the database"""
    registrations = UserRegistration.objects.select_related('user').all()
    return render(request, 'users/user_list.html', {'registrations': registrations})


def home(request):
    """Home page"""
    return render(request, 'index.html')
