from django.urls import path
from . import views
from Quiz.views import OpenQuesCreateView, MultQuesCreateView

urlpatterns = [
    path('addQues/multi/', MultQuesCreateView.as_view(), name='MultiQues-add'),
    path('addQues/open/', OpenQuesCreateView.as_view(), name='OpenQues-add'),
]


