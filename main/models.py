from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('pants', 'Pants'),
        ('balls', 'Balls'),
        ('gloves', 'Gloves'),
        ('kneepad', 'Kneepad'),
        ('socks', 'Socks'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    description = models.TextField(max_length=255)
    thumbnail = models.URLField
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='balls')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title