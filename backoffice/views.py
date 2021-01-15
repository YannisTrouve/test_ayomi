from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model  
from django.http import *
from django.views.generic import *
from django.conf import settings
from .forms import UserUpdateForm, UserCreateForm
from django.urls import reverse_lazy

User = get_user_model() #import of Django User model

class Register(CreateView):
  """
    Class to register a new User.
    The model is from the Django User Model.
    The form is specified in forms.py and if registration succeeded, return to login page. 
  """
  model = User
  form_class = UserCreateForm
  template_name='front/register.html'
  success_url = reverse_lazy('login')



class LoginView(TemplateView):
  """
    Class to Login to the application.
  """
  template_name = 'front/index.html'
  def post(self, request, **kwargs):
    """
      Take all arguments in the inputs and post it 
      to the Django user authentification system to be log in.
    """
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        #To login an user, it needs to be in the database
        login(request, user)
        return redirect( 'modifyEmail', username=username )
        #Redirect to the main page

    #Redirect to the login page
    return render(request, self.template_name)


class LogoutView(TemplateView):
  """
    Class to handle the the logout function.
    When the button "se déconnecter" triggered, the user is redirect to the login page.
  """
  template_name = 'front/index.html'
  
  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)


class UserUpdateView(UpdateView):
  """
    Class to update the User's information in the main page.
    The model is from the Django User Model.
    If the update is succeed, the user is returned to the main page, with his username in the url.
  """
  model = User
  form_class = UserUpdateForm
  template_name ='back/index.html'
  success_url = 'backoffice:username'
  #Slug variable is mandatory to push to the username in the url.
  slug_field='username'
  slug_url_kwarg ='username'

  def get_success_url(self):
    """
      Function to redirect properly to the main page.
      Avoid Disallowed redirect error.
    """
    username = self.request.user.username 
    return reverse_lazy( 'modifyEmail', kwargs={'username':username})





