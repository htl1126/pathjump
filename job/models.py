from __future__ import unicode_literals

from django.db import models


class JobPost(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    industry = models.CharField(max_length=50, blank=True)
    employment_type = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=50, blank=True)
    job_function = models.CharField(max_length=50, blank=True)
    company_logo = models.ImageField(upload_to='company_logo', blank=True) # same pic for
                                                               # same company
    tags = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title
