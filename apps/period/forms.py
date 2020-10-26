from django import forms
from django.forms import ModelForm

from .models import Period

class PeriodForm(forms.ModelForm):
	title = forms.CharField(max_length=100, required=True)

	class Meta:
		model = Period
		fields = ['title']
