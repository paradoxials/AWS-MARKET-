from django import forms
from .models import *

class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ('songtitle', 'artist')

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('firstname', 'lastname')