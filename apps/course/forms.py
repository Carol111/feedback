from django import forms
from django.forms import ModelForm

from .models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('created_at',)
