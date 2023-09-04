from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    otp_secret = models.CharField(max_length=16, blank=True, null=True)
    is_admin=models.BooleanField(default=False)
    email=models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    
    
