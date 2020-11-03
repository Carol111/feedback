from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Comment
from ..course.models import Course

class CommentForm(forms.ModelForm):
    course = forms.CharField(initial='')
    text = forms.CharField(max_length=200, initial='')

    class Meta:
        model = Comment
        fields = ['course', 'text']

    def clean_course(self):
        course = self.cleaned_data['course']

        try:
            course = Course.objects.get(code=course)
        except Course.DoesNotExist:
            course = None

        if course is None:
            raise forms.ValidationError(_('O código informado não corresponde a nenhum curso.'))

        return course
