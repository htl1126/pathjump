from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^post/', views.post, name='post'),
    url(r'^board/(?P<page_number>[0-9]+)', views.job_board,
        name='job_board'),
    url(r'^board/', views.job_board,
        name='job_board'),
    url(r'^show_post/(?P<job_id>[0-9]+)', views.show_post,
        name='show_post'),
]
