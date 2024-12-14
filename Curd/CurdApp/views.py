from django.shortcuts import render, redirect
from .import models
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    about = models.About.objects.all()

    return render(request, 'index.html', {'about':about})


def blog(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        content = request.POST['content']
        blog_image = request.FILES['blog_image']
        url = request.POST['url']
        models.Blog.objects.create(user = user, title = title, content = content, blog_image = blog_image, url = url)
        messages.success(request, message='Your blog is uploded successfully')
        return redirect('index')
    
    return render(request, 'blog.html', {'blog': blog})

def blog_list(request):
    blogs = models.Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    return render(request, 'blog_detail.html', {'blogs':blogs})

def blog_delete(request, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        blogs.delete()
        messages.success(request, message='Your blog is deleted is sucessfully')
        return redirect('blog_list')
    return render(request, 'blog_delete.html', {'blogs':blogs})

def blog_update(request, blog_id):
    blogs = models.Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        blogs.title = request.POST.get('title','')
        blogs.content = request.POST.get('content','')
        if request.FILES.get('blog_image'):
            blogs.blog_image = request.FILES['blog_image']
        blogs.url = request.POST.get('url','')
        blogs.save()
        return redirect('blog_list')
    
    return render(request, 'blog_update.html',{'blogs': blogs})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request= request, user=user)
            return redirect('index')
        else:
            messages.warning(request = request , message="Incorrect username or password")
    return render(request, 'login_view.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.warning(request=request, message="Username already taken")
            elif User.objects.filter(email = email).exists():
                messages.warning(request=request, message="Email already registerd")
            else:
                User.objects.create_user(username=username, email=email, password=password, is_staff = True)
                user = authenticate(username = username, password= password)
                login(request=request, user=user)
                messages.success(request=request, message="Your are successfully registerd")
                return redirect('index')
        else:
            messages.warning(request=request, message="password is not match")

    
    return render(request, 'signup.html')


def logut_view(request):
    logout(request=request)
    messages.success(request=request, message="Your are successfully logout")
    return redirect('login_view')

def student(request):
    # if request.method == 'POST':
    #     std_name = request.POST['std_name']
    #     std_father_name = request.POST['std_father_name']
    #     std_roll_no = request.POST['std_roll_no']
    #     std_class = request.POST['std_class']
    #     english = request.POST['english']
    #     urdu = request.POST['urdu']
    #     computer = request.POST['computer']
    #     islmyast = request.POST['islmyast']
    #     pak_study = request.POST['pak_study']
    #     models.Student.objects.create(std_name = std_name, std_father_name = std_father_name, std_roll_no = std_roll_no, std_class = std_class, english = english, urdu = urdu, computer = computer, islmyast = islmyast, pak_study = pak_study)

    # return render(request, "student.html", {'students':student})
    student = models.Student.objects.all()
    context = {
        'students': student
    }
    return render(request, 'student.html', context)



