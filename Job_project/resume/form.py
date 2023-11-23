from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["user", "first_name", "surname", "location", "job_title"]#"upload_resume"]
        #exclude=('user')