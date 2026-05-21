from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    """Custom user registration model extending Django's User model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.email}"

    class Meta:
        ordering = ['-created_at']
