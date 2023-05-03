from django.views.generic import ListView, CreateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    form_class = TaskForm
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
