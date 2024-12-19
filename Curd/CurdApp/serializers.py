from rest_framework import serializers
from .models import About, Blog, Student, Employe, Job
from django.contrib.auth.models import User

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
