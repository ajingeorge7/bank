from django import forms
from.models import form

class forma(forms.ModelForm):
    class Meta:
        model=form
        fields=['name','dob','age','phone']
