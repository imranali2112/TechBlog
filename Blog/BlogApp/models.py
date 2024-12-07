from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_image/", blank=True)
    upload_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}'    
    
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    phone_no = models.BigIntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to="user_profile/")

    
    def __str__(self):
        return f'{self.user}'