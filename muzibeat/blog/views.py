from django.shortcuts import render
from muzibeat.account.models import Post_user
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Post_user.objects.get(id= image_id)
            if action == 'like':
                Post_user.user_like.add(request.user)
            else:
                Post_user.user_like.remove(request.user)
            return JsonResponse({'status': 'OK'})
        except:
            pass
    return JsonResponse({'status': 'Error'})