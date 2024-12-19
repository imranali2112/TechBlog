from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_image/', blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.user}'


class Student(models.Model):
    std_name = models.CharField(max_length=200)
    std_father_name = models.CharField(max_length=200)
    std_roll_no = models.CharField(max_length=200)
    std_class = models.IntegerField()
    english = models.IntegerField(default=100)
    urdu = models.IntegerField(default=100)
    computer_science = models.IntegerField(default=100)
    islmyast = models.IntegerField(default=100)
    maths = models.IntegerField(default=100)
    pak_study = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.std_name} by {self.std_roll_no}'


    @property
    def avg_marks(self):
        averg = self.english + self.urdu + self.computer_science + self.islmyast + self.maths + self.pak_study / 6
        return round(averg, 2)
    
    @property
    def std_percent(self):
        marks = self.english + self.urdu + self.maths + self.computer_science + self.islmyast + self.pak_study
        percentage = marks * 100 / 600
        return round(percentage, 2)
    
    @property
    def total_marks(self):
        total = self.english + self.urdu + self.maths + self.computer_science + self.islmyast + self.pak_study
        return total
    
class Employe(models.Model):
    employe_name = models.CharField(max_length=200)
    employe_dep = models.CharField(max_length=200)
    employe_age = models.CharField(max_length=200)
    employe_address = models.CharField(max_length=200)

    def __str__(self):
        return self.employe_name
    

class Job(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField()
    dep = models.CharField(max_length=200)

    def __str__(self):
        return self.title

