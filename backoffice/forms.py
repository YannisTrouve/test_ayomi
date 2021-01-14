from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name']


