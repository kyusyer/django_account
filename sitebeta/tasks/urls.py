from django.http import HttpResponse
from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path("", views.index, name="index"),
    path("addtasks", views.addtasks, name='addtasks'),

]