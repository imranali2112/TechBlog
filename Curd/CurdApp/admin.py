from django.contrib import admin
from .import models
# Register your models here.
admin.site.register(models.About)
admin.site.register(models.Blog)

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['std_name', 'std_father_name', 'std_class', 'english', 'urdu', 'computer_science', 'maths', 'islmyast','pak_study', 'total_marks','avg_marks','std_percent']
    