from django.shortcuts import render


def profile(request):
    return render(request, 'account/profile.html', {})
