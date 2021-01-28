from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Meow


@login_required
def meowing(request):
    userids = [request.user.id]
    for meower in request.user.meowprofile.follows.all():
        userids.append(meower.user.id)

    meows = Meow.objects.filter(created_by_id__in=userids)
    return render(request, 'Meowing.html', {'meows': meows})