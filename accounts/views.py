from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

#Only username and password
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#add more fields
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    
    #for ordering display fields
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
    
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
