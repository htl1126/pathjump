from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from .models import User, UserProfile
from django.contrib.auth import login, authenticate


def onboard(request):
    return render(request, 'account/onboard.html', {})


def profile(request):
    return render(request, 'account/profile.html',
                  {'user_form': request.user,
                   'profile_form': request.user.profile})


def show_profile(request):
    return render(request, 'account/show_profile.html',
                  {'user_form': request.user,
                   'profile_form': request.user.profile})


# ref: http://stackoverflow.com/questions/32942529/django-not-null-constraint
#             -failed-userprofile-user-id-in-case-of-uploading-a-fil
# ref: http://stackoverflow.com/questions/12828913/django-how-to-create-table
#             -and-then-update-database-through-them
def update(request):
    userform_obj = User.objects.get(username=request.user.username)
    profile_obj = UserProfile.objects.get(user_id=userform_obj.id)
    update_success = False
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            update_success = True
        else:
            print profile_form.errors
            profile_form = UserProfileForm()
    else:
        profile_form = UserProfileForm(instance=profile_obj)
    return render(request, 'account/update.html',
                  {'profile_form': profile_form,
                   'update_success': update_success})


# ref: http://stackoverflow.com/questions/33041592/redirect-to-home-as
#             -a-logged-in-user-after-successful-registration
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
            password = request.POST['password']
            authenticated = authenticate(username=user.username,
                                         password=password)
            if authenticated:
                login(request, authenticated)
                return redirect('/')
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
