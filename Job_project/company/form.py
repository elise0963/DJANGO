from django import forms 
from .models import Company

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model =  Company
        fields = ["user", "name", "est_date", "city", "state"]
        #exclude = ('user')

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model =  Company
        fields = ["user", "name", "est_date", "city", "state"]
        #exclude = ('user',)