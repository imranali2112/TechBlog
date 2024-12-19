from rest_framework import viewsets
from .serializers import AboutSerializer, UserSerializer, BlogSerializer, StudentsSerializer, EmployeSerializer, JobSerializer
from .models import About, User, Blog, Student, Employe, Job

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BlogViewSets(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
