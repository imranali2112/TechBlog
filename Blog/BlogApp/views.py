from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Blog, Comment
from .import models
from django.contrib import messages
from django.contrib.auth import decorators
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request=request, message="Username already taken")
            elif User.objects.filter(email = email).exists():
                messages.warning(request=request, message="Email already registered")
            else:
                User.objects.create_user(username=username, email=email, password=password, is_staff=True)
                user = authenticate(username = username, password = password)

                login(request=request, user = user)
                return redirect('user_profile')
        else:
            messages.warning(request=request, message="Password or username incorrect. Please try again")

    return render(request, 'signup_view.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username = username, password = password)
        if user is not None:
            login(request=request, user = user)
            return redirect('index')
        else:
            messages.warning(request=request, message="Password or username is incorrect")
    return render(request, 'login_view.html')

def logout_view(request):
    logout(request=request)
    messages.success(request=request, message="Your are sucessfully logout")
    return redirect('index')

def user_profile(request):
    if request.method == 'POST':
        user = request.user
        bio = request.POST['bio']
        phone_no = request.POST['phone_no']
        address = request.POST['address']
        image = request.FILES['image']
        models.User_Profile.objects.create(user = user, bio = bio, phone_no = phone_no, address = address, image = image)
        messages.success(request=request, message="Your profile is sucessfully saved")
        return redirect('index')
    return render(request, 'user_profile.html')

def profile(request):
    profiles = models.User_Profile.objects.filter(user = request.user)
    context = {
        'profile': profiles
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    profile = models.User_Profile.objects.get(user = request.user)
    if request.method == 'POST':
        profile.bio = request.POST.get('bio','')
        profile.phone_no = request.POST.get('phone_no','')
        profile.address = request.POST.get('address','')
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
        profile.save()

        return redirect('profile')
    return render(request, 'edit_profile.html',{'profile':profile})



def about(request):
    about = models.About.objects.all()
    return render(request, 'about.html', {'abouts': about})


def blog(request):
    blogs = models.Blog.objects.all().order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def blog_detail(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        content = request.POST.get('content','')
        models.Comment.objects.create(user = request.user, blog = blog, content = content)
    context = {
        'blog': blog,
    }
    
    return render(request, 'blog_detail.html', context)

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        models.Contact.objects.create(full_name = full_name, email = email, subject = subject, message = message)
        messages.success(request=request, message='Your message is sucessfully sended')
        return redirect('contact')
    return render(request, 'contact.html')