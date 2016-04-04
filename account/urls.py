from django.conf.urls import url
import django.contrib.auth.views

from . import views

urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
    url(r'^login/', django.contrib.auth.views.login, name='login',
        kwargs={'template_name': 'account/login.html'}),
    url(r'^logout/', django.contrib.auth.views.logout, name='logout',
        kwargs={'next_page': '/'}),
    url(r'^register/', views.register, name='register'),
]
