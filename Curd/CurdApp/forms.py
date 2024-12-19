from django import forms
from .import models
from .models import Job

class EmployeForm(forms.Form):
    employe_name = forms.CharField(label="Employee Name", required=True)
    employe_dep = forms.CharField(label="Employee Deparment")
    employe_age = forms.CharField(label="Employee Age")
    employe_address = forms.CharField(label="Employee Address")


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'decription', 'dep']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'Enter Job Title'}),
            'decription': forms.Textarea(attrs={'class': 'form-control col-md-6', 'placeholder': 'Write Job Decription'}),
            'dep': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'Enter your dep...'}),
        }
        lable = {
            'title':'Job Title'
        }
         