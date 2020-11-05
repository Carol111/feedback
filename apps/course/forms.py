from django import forms
from django.forms import ModelForm

from .models import Course

class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=100, initial='')
    code = forms.CharField(max_length=20, initial='')

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('user',)
