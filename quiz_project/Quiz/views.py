from django.shortcuts import render
from django.views.generic.edit import CreateView
from Quiz.forms import *
from Quiz.models import *

# Create your views here.
class OpenQuesCreateView(CreateView):
    model = OpenQuesModel
    class_form = addOpenQuestionform
    fields = '__all__'
    template_name  = 'Quiz/addQues.html'
    success_url = '/admin/Quiz/openquesmodel/'

class MultQuesCreateView(CreateView):
    model = MultQuesModel
    class_form = addMultiQuestionform
    fields = '__all__'
    template_name  = 'Quiz/addQues.html'
    success_url = '/admin/Quiz/openquesmodel/'
