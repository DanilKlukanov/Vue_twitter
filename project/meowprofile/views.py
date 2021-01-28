from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .forms import MeowProfileForm


def meowerprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }

    return render(request, 'MeowerProfile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = MeowProfileForm(request.POST, request.FILES, instance=request.user.meowprofile)

        if form.is_valid():
            form.save()

            return redirect('meowerprofile', username=request.user.username)
    else:
        form = MeowProfileForm(instance=request.user.meowprofile)

    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'EditProfile.html', context)


@login_required
def follow_meower(request, username):
    user = get_object_or_404(User, username=username)
    request.user.meowprofile.follows.add(user.meowprofile)
    return redirect('meowerprofile', username=username)


@login_required
def unfollow_meower(request, username):
    user = get_object_or_404(User, username=username)
    request.user.meowprofile.follows.remove(user.meowprofile)
    return redirect('meowerprofile', username=username)


def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'Followers.html', {'user': user})


def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'Follows.html', {'user': user})
