from django.db import models

# Create your models here.
class OpenQuesModel(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250, null=True)    
    correct_ans = models.CharField(max_length=250)    

class MultQuesModel(models.Model):
    question = models.CharField(max_length=250)
    opt1 = models.CharField(max_length=200,null=True)
    opt2 = models.CharField(max_length=200,null=True)
    opt3 = models.CharField(max_length=200,null=True)
    opt4 = models.CharField(max_length=200,null=True)
    correct_ans = models.CharField(max_length=250)
