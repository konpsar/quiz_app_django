from django.shortcuts import render
from django.views.generic.edit import CreateView
from Quiz.models import *

# Create your views here.
class OpenQuesCreateView(CreateView):
    model = OpenQuesModel
    fields = '__all__'
    template_name  = 'Quiz/addQues.html'


class MultQuesCreateView(CreateView):
    model = MultQuesModel
    fields = '__all__'
    template_name  = 'Quiz/addQues.html'
