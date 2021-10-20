from django.db import models
    
class userManager(models.Manager):
    def validate_data():
        pass

class devices(models.Model):
    name= models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    touch = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class locations(models.Model):
    lattitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class tickets(models.Model):
    ticket = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class users(models.Model):
    IP = models.CharField(max_length=25)
    device = models.ForeignKey(devices, related_name="device_type", on_delete = models.CASCADE)
    location = models.ForeignKey(locations, related_name="geo_location", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
