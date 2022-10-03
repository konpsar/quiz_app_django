from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
class HomeView(TemplateView):
    template_name  = 'home/welcome.html'
    extra_context = {'today':datetime.today()}
    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name  = 'home/signup.html'
    extra_context = {}
    
