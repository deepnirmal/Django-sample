from django.shortcuts import render
from django.views.generic import TemplateView


from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from api.models import Task
from api.forms import TodoForm


class HomePageView(TemplateView):

    def get(self, request, **kwargs):

        task_list = Task.objects.all()

        context = {'task_list': task_list}

        return render(request, 'index.html', context)

    def addTask(request):

        print("Request got here")
        # print(request.__dict__)
        new_task = Task(title=request.POST.get('title'),due_date=request.POST.get('date'),status=request.POST.get('status'))
        print("Got the request correctly")
        new_task.save()

        return redirect('home')


class AboutPageView(TemplateView):
    template_name = "about.html"


