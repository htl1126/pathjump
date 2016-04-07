from django.shortcuts import render
from .forms import UserForm, UserProfileForm


def profile(request):
    return render(request, 'account/profile.html',
                  {'user_form': request.user,
                   'profile_form': request.user.profile})


def register(request):
    registered = False
    user_exist = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
            user_exist = True
            user_form = UserForm()
            profile_form = UserProfileForm()
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'account/register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered, 'user_exist': user_exist})
