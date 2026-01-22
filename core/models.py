from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def str(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    def str(self):
        return self.name

class Item(models.Model):
    STATUS_CHOICES = [('lost', 'Потеряно'), ('found', 'Найдено')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    date_lost_found = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=200)
    is_resolved = models.BooleanField(default=False)
    
    def str(self):
        return f"{self.title} ({self.get_status_display()})"    