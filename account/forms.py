from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, 2016)))

    class Meta:
        model = UserProfile
        fields = ('picture', 'website', 'university', 'birthday', 'country',
                  'city', 'address', 'zipcode', 'tags')
