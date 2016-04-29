from django.shortcuts import render
from .forms import JobPostForm


def post(request):
    post_success = False
    if request.method == 'POST':
        job_form = JobPostForm(data=request.POST)

        if job_form.is_valid():
            job = job_form.save()
            job.save()
            post_success = True
        else:
            print job_form.errors
            job_form = JobPostForm()
    else:
        job_form = JobPostForm()
    return render(request, 'job/post.html',
                  {'job_form': job_form, 'post_success': post_success})
