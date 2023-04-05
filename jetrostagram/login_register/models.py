from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class feeds(models.Model):
    username = models.CharField(max_length = 20)
    image = models.ImageField(upload_to="pics")


# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')


class Post(models.Model):
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='posts/')


class Customer(models.Model):
     user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
     profile_pic = models.ImageField(blank=True, null=True)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    title = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
