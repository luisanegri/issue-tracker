from django.conf.urls import url, include
from .views import all_issues, get_detail, create_issue, my_issues, edit_issue, create_comment, edit_comment, delete_issue, upvote


urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^myissues$', my_issues, name='my_issues'),
    url(r'^edit/(?P<pk>\d+)$', edit_issue, name='edit'),
    url(r'^new$', create_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/$', get_detail, name='get_detail'),
    url(r'^(?P<pk>\d+)/new/$', create_comment, name='create_comment'),
    url(r'^(?P<pk>\d+)/edit/$', edit_comment, name='edit_comment'),
    url(r'^(?P<pk>\d+)/delete/$', delete_issue, name='delete_issue'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote, name='upvote'),
 
]