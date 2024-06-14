from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Unique related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='custom_user_permissions'
    )


class Task(models.Model):
    name = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=10, default='pending')
