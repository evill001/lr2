from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'myapp/index.html', {
        'title': 'Главная страница сайта', 'tasks': tasks})


def rasp(request):
    return render(request, 'myapp/rasp.html')


def news(request):
    return render(request, 'myapp/news.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/create.html', context)


class Del(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'myapp/task-delete.html'


class Upd(UpdateView):
    model = Task
    template_name = 'myapp/create.html'
    form_class = TaskForm
    success_url = '/'
