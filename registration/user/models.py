from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_wastecollector = models.BooleanField(default=False)
    is_wasterecycler = models.BooleanField(default=False)

class WasteCollector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='waste_collector')
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=200)
    location = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.first_name

class WasteRecycler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='waste_recycler')
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=200)


    def __str__(self):
        return self.first_name
