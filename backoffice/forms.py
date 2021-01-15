from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib.auth.models import User


User = get_user_model() #import of Django User model

class UserCreateForm(UserCreationForm):
	"""
		This class inherits from Django User model into a form to create an user.
		You don't need clean_data function for validation errors, it inherits from Django's User model
		First name, last name and email were added and now the email is mandatory.
	"""


	prénom = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
	nom = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
	email = forms.EmailField(max_length=254, required=True, help_text='Obligatoire.')

	class Meta:
		"""
			Meta class to configure the form with all email, first name, last name, username, password 1 & 2 attribute.
			It take the Django User's modek
		"""
		model = User
		fields = ['email','first_name','last_name','username', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):
	"""
		Class to convert the Django User model into a form to update an user.
		This class inherits from Django's ModelForm.
		Only the email is updated. To update other user's attribute, you need to add them to "fields".
	"""

	class Meta:
		model = User
		fields = ['email']

	def clean(self):
		"""
			This function is used for basic field validation.
			You need to put a valid email adresse to validate the form.
		"""
		data = self.cleaned_data
		if data.get('email', None):
			return data
		else:
			raise forms.ValidationError('Vous devez rentrer une adresse mail.')


