from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegistrationForm(forms.Form):
    """Form for user registration with validation"""
    
    username = forms.CharField(
        label='Username',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autocomplete': 'off'
        })
    )
    
    email = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'autocomplete': 'off'
        })
    )
    
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
    
    confirm_password = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })
    )
    
    def clean_username(self):
        """Validate username uniqueness and format"""
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken. Please choose another.')
        
        if len(username) < 3:
            raise ValidationError('Username must be at least 3 characters long.')
        
        if not re.match('^[a-zA-Z0-9_]+$', username):
            raise ValidationError('Username can only contain letters, numbers, and underscores.')
        
        return username
    
    def clean_email(self):
        """Validate email uniqueness"""
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        
        return email
    
    def clean_password(self):
        """Validate password strength"""
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        
        if not any(char.isupper() for char in password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        
        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least one digit.')
        
        return password
    
    def clean(self):
        """Validate password and confirm_password match"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match. Please try again.')
        
        return cleaned_data


class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField(
        label='Username',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password'
        })
    )
