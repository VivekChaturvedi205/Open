from django.shortcuts import (get_object_or_404,
                              render,
                              redirect)
from .models import Task
from .forms import TaskForm,TaskForm1
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    data = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TaskForm()

    hell = {
        "data": data,
        "forms": form,
    }

    return render(request, 'home.html', hell)


def login(request):
    res = render(request, 'login.html')
    return HttpResponse(res)


def lprocess(request):
    if request.method == 'POST':
        # check User is exist
        UserName = request.POST['UserName']
        Password = request.POST['Password']
        user = auth.authenticate(username=UserName, password=Password)
        if user is not None:
            auth.login(request, user)
            request.session['UserName'] = UserName
            return redirect("https://app.powerbi.com/view?r=eyJrIjoiZWE3Y2RjODItZDY3OC00NDEzLTgyMTctNjQyMWEzYmE3ODE4IiwidCI6ImUxOTk3OThlLWEyOTEtNGQ1ZC05NjM0LTI4Y2FkZDMxNTM5NyJ9&embedImagePlaceholder=true")
        else:
            return render(request, 'login.html', {'error': "Invalid login Credentials!!"})
    else:
        res = render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Task, id=id)
    form = TaskForm1(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context["form"] = form

    return render(request, "update.html", context)
