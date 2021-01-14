from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib.auth.models import User


User = get_user_model()

class UserCreateForm(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
	email = forms.EmailField(max_length=254, help_text='Obligatoire.')

	class Meta:
		model = User
		fields = ['email','first_name','last_name','username', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email']

	def clean(self):
		data = self.cleaned_data
		if data.get('email', None):
			return data
		else:
			raise forms.ValidationError('Vous devez rentrer une adresse mail.')


