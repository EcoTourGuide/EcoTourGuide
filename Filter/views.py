from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm


# Temporary view for demonstration without requiring login
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user_id=user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)

    return render(request, 'filter/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    })
