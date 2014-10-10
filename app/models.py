from django.db import models

# Create your models here.

class ApiKey(models.Model):
    api_key = models.CharField(max_length=255,unique=True)
    current_status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)

class Coords(models.Model):
    user_api = models.ForeignKey(ApiKey)
    coords = models.TextField()
    message = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=True)