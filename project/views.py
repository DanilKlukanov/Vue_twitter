from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def front(request):
    return render(request, 'FrontBase.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('front')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
