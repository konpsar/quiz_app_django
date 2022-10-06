from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
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


class QuesListView(ListView):
    model = MultQuesModel
    context_object_name = "multiQs"
    template_name = "Quiz/multi_ques_list.html"
    
    #Search on ccbv.co.uk/projects/Django/3.1/ to get help on class views and find what 
    #we should alter in order to get only specific user's notes

    def get_queryset(self):
        return MultQuesModel.objects.all()
    
class OpenQuesListView(ListView):
    model = OpenQuesModel
    context_object_name = "openQs"
    template_name = "Quiz/open_ques_list.html"
    
    #Search on ccbv.co.uk/projects/Django/3.1/ to get help on class views and find what 
    #we should alter in order to get only specific user's notes

    def get_queryset(self):
        return OpenQuesModel.objects.all()
    
    