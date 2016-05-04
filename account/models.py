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
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=update_filename, blank=True)
    university = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(default=timezone.now)
    country = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=20, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
