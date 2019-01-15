from django import  forms
from .models import Sample_Data


class RawForm(forms.Form):
	name = forms.CharField()
	age = forms.IntegerField()