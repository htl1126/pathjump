from __future__ import unicode_literals

import os
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def update_filename(instance, filename):
    path = 'profile_image/'
    ext = filename.split('.')[-1]
    format = '{0}.{1}'.format(instance.user.username, ext)
    return os.path.join(path, format)


# ref: http://stackoverflow.com/questions/20613315/
#      get-rid-of-get-profile-in-a-migration-to-django-1-6
# ref: http://www.tangowithdjango.com/book17/chapters/login.html
# ref: http://stackoverflow.com/questions/32167455/django-how-to-
#      get-userprofile-instances-in-template-having-onetoone-relationsh
# ref: http://stackoverflow.com/questions/28748281/extending-user-profile
#      -in-django-1-7
# ref: http://stackoverflow.com/questions/2680391/in-django-changing-the
#      -file-name-of-uploading-file
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='profile',
                                primary_key=True)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to=update_filename, blank=True)
    university_1 = models.CharField(max_length=30, blank=True)
    university_grad_date_1 = models.CharField(max_length=20, blank=True)
    major_1 = models.CharField(max_length=20, blank=True)
    gpa_1 = models.CharField(max_length=10, blank=True)
    university_2 = models.CharField(max_length=30, blank=True)
    university_grad_date_1 = models.CharField(max_length=20, blank=True)
    university_grad_date_2 = models.CharField(max_length=20, blank=True)
    major_2 = models.CharField(max_length=20, blank=True)
    gpa_2 = models.CharField(max_length=10, blank=True)
    university_3 = models.CharField(max_length=30, blank=True)
    university_grad_date_1 = models.CharField(max_length=20, blank=True)
    university_grad_date_3 = models.CharField(max_length=20, blank=True)
    major_3 = models.CharField(max_length=20, blank=True)
    gpa_3 = models.CharField(max_length=10, blank=True)
    company_1 = models.CharField(max_length=50, blank=True)
    job_title_1 = models.CharField(max_length=50, blank=True)
    job_desc_1 = models.CharField(max_length=200, blank=True)
    company_2 = models.CharField(max_length=50, blank=True)
    job_title_2 = models.CharField(max_length=50, blank=True)
    job_desc_2 = models.CharField(max_length=200, blank=True)
    company_3 = models.CharField(max_length=50, blank=True)
    job_title_3 = models.CharField(max_length=50, blank=True)
    job_desc_3 = models.CharField(max_length=200, blank=True)
    about_me = models.CharField(max_length=100, blank=True)
    fun_fact = models.CharField(max_length=100, blank=True)
    skill = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    user_val = models.CharField(max_length=50, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
