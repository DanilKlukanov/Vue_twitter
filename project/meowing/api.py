import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Meow


@login_required
def api_add_meow(request):
    data = json.loads(request.body)
    body = data['body']

    meow = Meow.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})
