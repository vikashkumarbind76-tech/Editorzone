from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Service(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic'),
        ('professional', 'Professional'),
        ('premium', 'Premium'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.CharField(max_length=50)
    features = models.TextField(help_text="Features separated by commas")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.package_type}"

    def get_features_list(self):
        return [feature.strip() for feature in self.features.split(',')]

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50)
    completion_time = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    client_name = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()
    deadline = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    special_requirements = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} - {self.project_title}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"