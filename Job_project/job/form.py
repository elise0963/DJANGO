from django import forms
from .models import Job

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        #fields = ["user", "company", "title", "salary", "location", "requirements", "ideal_candidate", "is_available"]
        exclude = ('user', 'company')
        
        
class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        #fields = ["user", "company", "title", "salary", "location", "requirements", "ideal_candidate", "is_available"]
        exclude = ('user', 'company')