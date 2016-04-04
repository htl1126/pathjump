from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def profile(request):
    return render(request, 'account/profile.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})
