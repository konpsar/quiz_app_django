from django.forms import ModelForm
from .models import *

class addOpenQuestionform(ModelForm):
    class Meta:
        model=OpenQuesModel
        fields="__all__"
        
class addMultiQuestionform(ModelForm):
    class Meta:
        model=MultQuesModel
        fields="__all__"
        