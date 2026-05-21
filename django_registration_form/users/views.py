from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import RegistrationForm
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


def user_list(request):
    """List all registered users from the database"""
    registrations = UserRegistration.objects.select_related('user').all()
    return render(request, 'users/user_list.html', {'registrations': registrations})


def home(request):
    """Home page"""
    return render(request, 'index.html')
