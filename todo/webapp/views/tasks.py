
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Task


class IndexView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"