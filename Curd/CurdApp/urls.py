from django.urls import path, include
from .import views
from .routers import router
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog_detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog_delete/<int:blog_id>', views.blog_delete, name='blog_delete'),
    path('blog_update/<int:blog_id>/', views.blog_update, name='blog_update'),
    path('login_view/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('logut_view/', views.logut_view, name='logut_view'),
    path('student/', views.student, name= 'student'),
    path('employee', views.employe, name='employee'),
    path('job', views.job, name = 'job'),
    path('api/', include(router.urls)),

]