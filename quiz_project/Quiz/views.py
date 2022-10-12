from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from Quiz.forms import *
from Quiz.models import *
from random import sample

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
    
    
class QuizView(TemplateView):
    template_name = 'Quiz/quiz_page.html'
    # rand_qs = sample(list(MultQuesModel.objects.all()), 10)
    multi_questions = MultQuesModel.objects.order_by("?").all()[:10]

    def post(self, request, *args, **kwargs):
        multi_questions = self.multi_questions #random order and take first
        # multi_questions = self.rand_qs #random order and take first
        score=0
        wrong=0
        correct=0
        total=0
        for q in multi_questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.correct_ans)
            print()  
            if q.correct_ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }      
        return render(request, 'Quiz/results.html', context)

    def get(self, request, *args, **kwargs):
        multi_questions = self.multi_questions
        # multi_questions = self.rand_qs
        context = {'multi_questions': multi_questions}
        return render(request, self.template_name, context)