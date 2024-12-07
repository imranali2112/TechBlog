from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup_view', views.signup_view, name='signup_view'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]