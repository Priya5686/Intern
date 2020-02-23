from django.shortcuts import render, redirect
from myapp.forms import RegisterForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'myapp/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else:
        form = RegisterForm()

        args = {'form': form}
        return render(request, 'myapp/reg_form.html', args)

