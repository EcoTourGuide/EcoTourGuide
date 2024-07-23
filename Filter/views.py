from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import UserForm, UserProfileForm, ProfilePhotoForm
from .models import History, UserProfile

@login_required
@csrf_exempt
def record_visit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        site_name = data.get('site_name')
        url = data.get('url')
        History.objects.create(user=request.user, site_name=site_name, url=url)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)
    photo_form = ProfilePhotoForm()

    return render(request, 'filter/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'photo_form': photo_form
    })

@login_required
def profile_photo_upload(request):
    if request.method == 'POST' and 'profile_photo' in request.FILES:
        profile = request.user.userprofile
        profile.profile_photo = request.FILES['profile_photo']
        profile.save()
        return JsonResponse({'status': 'success', 'photo_url': profile.profile_photo.url})
    return JsonResponse({'status': 'error'})

@login_required
def profile_information(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'filter/tabs/profile_information.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def user_history(request):
    visited_sites = History.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'filter/tabs/user_history.html', {'visited_sites': visited_sites})

@login_required
def newsletter_subscription(request):
    return render(request, 'filter/tabs/newsletter_subscription.html')

@login_required
def manage_notifications(request):
    return render(request, 'filter/tabs/manage_notifications.html')
