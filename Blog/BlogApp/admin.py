from django.contrib import admin
from .import models
# Register your models here.
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','author']

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','upload_at']

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name','email', 'subject']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(models.User_Profile)
class User_ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']