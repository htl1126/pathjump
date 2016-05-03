from django.shortcuts import render
from .forms import JobPostForm
from .models import JobPost


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


def job_board(request, page_number=None):
    if not page_number:
        page_number = 1
    else:
        page_number = int(page_number)
    page_size = 3  # at most 3 jobposts in a page, hardcoded so far
    job_post_size = JobPost.objects.count()
    min_page_number = 1
    max_page_number = job_post_size / page_size
    if job_post_size % 3 != 0:
        max_page_number += 1
    page_number_list = range(min_page_number, max_page_number + 1)
    first_post_in_page = (page_number - 1) * page_size
    if first_post_in_page > job_post_size:
        page_number = 1
    if page_number * page_size > job_post_size:
        job_post_list = JobPost.objects.order_by('pk')[
            first_post_in_page:job_post_size]
    else:
        job_post_list = JobPost.objects.order_by('pk')[
            first_post_in_page:page_number * page_size]
    return render(request, 'job/board.html',
                  {'job_list': job_post_list,
                   'page_number_list': page_number_list})


def show_post(request, job_id):
    job_post = JobPost.objects.get(pk=int(job_id))
    return render(request, 'job/show_post.html', {'job_post': job_post})
