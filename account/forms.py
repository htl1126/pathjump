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
    university_grad_date_1 = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, 2016)))
    university_grad_date_2 = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, 2016)))
    university_grad_date_3 = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, 2016)))

    class Meta:
        model = UserProfile
        fields = ('picture', 'university_grad_date_1', 'major_1', 'gpa_1',
                  'university_grad_date_2', 'major_2', 'gpa_2',
                  'university_grad_date_3', 'major_3', 'gpa_3',
                  'company_1', 'job_title_1', 'job_desc_1',
                  'company_2', 'job_title_2', 'job_desc_2',
                  'company_3', 'job_title_3', 'job_desc_3',
                  'about_me', 'fun_fact', 'skill', 'birthday', 'country',
                  'city', 'address', 'zipcode', 'user_val')
