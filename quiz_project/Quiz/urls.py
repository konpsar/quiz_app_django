from django.urls import path
from . import views
from Quiz.views import OpenQuesCreateView, MultQuesCreateView

urlpatterns = [
    path('Ques/add/multi/', MultQuesCreateView.as_view(), name='MultiQues-add'),
    path('Ques/add/open/', OpenQuesCreateView.as_view(), name='OpenQues-add'),
    path('Ques/list/multi', views.QuesListView.as_view(), name="multiQues.list"),
    path('Ques/list/open', views.OpenQuesListView.as_view(), name="openQues.list"),

]


