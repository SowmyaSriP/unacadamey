from django import forms
from .models import *
class courseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'
class prosForm(forms.ModelForm):
    class Meta:
        model = pros
        fields = '__all__'