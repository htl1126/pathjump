from django import forms
from .models import JobPost


class JobPostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 30, 'rows': 20}))

    class Meta:
        model = JobPost
        fields = ('title', 'company', 'location', 'description', 'industry',
                  'employment_type', 'experience', 'job_function',
                  'company_logo', 'tags')
