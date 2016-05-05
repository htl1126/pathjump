from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture', 'major_1', 'gpa_1',
                  'major_2', 'gpa_2',
                  'major_3', 'gpa_3',
                  'company_1', 'job_title_1', 'job_desc_1',
                  'company_2', 'job_title_2', 'job_desc_2',
                  'company_3', 'job_title_3', 'job_desc_3',
                  'about_me', 'fun_fact', 'skill', 'country',
                  'city', 'address', 'zipcode', 'user_val')
