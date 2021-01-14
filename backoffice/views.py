from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import *
from django.views.generic import *
from django.conf import settings
from .forms import UserUpdateForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

User = get_user_model()

class LoginView(TemplateView):

  template_name = 'front/index.html'
  redirect_name = 'back/index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return redirect( 'modifyEmail', username=username )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'front/index.html'

  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)


class UserUpdateView(UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name ='back/index.html'
	success_url = 'backoffice:username'
	slug_field='username'
	slug_url_kwarg ='username'

	def get_success_url(self):
		username = self.request.user.username 
		return reverse_lazy( 'modifyEmail', kwargs={'username':username})






# class ProfilView(UpdateView):
# 	model = User
# 	from_class=UserUpdateForm
# 	template_name = 'back/index.html'

# 	def form_valid(self, form):
# 		user = form.save(commit=True)
# 		password = form.cleaned_data['password']
# 		user.set_password(password)
# 		user.save()
# 		return redirect(self.template_name)

# 	def get_object(self):
# 		user = form.save(commit=True)
# 		return user.username
