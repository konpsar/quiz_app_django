from django.contrib import admin

from quiz_project.Quiz.models import MultQuesModel, OpenQuesModel

# Register your models here.
admin.site.register(OpenQuesModel)
admin.site.register(MultQuesModel)
