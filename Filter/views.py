from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm, UserProfileForm, ProfilePhotoForm
from .models import History, UserProfile

@csrf_exempt
@login_required
def record_visit(request):
    if request.method == "POST":
        data = json.loads(request.body)
        site_name = data.get("site_name")
        url = data.get("url")

        # Save the visit to the database
        History.objects.create(user=request.user, site_name=site_name, url=url)
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "fail"})

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        if 'profile_photo' in request.FILES:
            # Handle profile photo upload
            photo_form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user.userprofile)
            if photo_form.is_valid():
                photo_form.save()
                messages.success(request, 'Profile photo updated successfully.')
            else:
                messages.error(request, "There are errors in your photo upload form. Please correct them and try again.")
            return redirect('profile')
        else:
            # Handle profile information update
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
            else:
                messages.error(request, "There are errors in your form. Please correct them and try again.")
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        photo_form = ProfilePhotoForm()

    return render(request, 'filter/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'photo_form': photo_form
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
