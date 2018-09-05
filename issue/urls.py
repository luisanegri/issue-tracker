from django.conf.urls import url, include
from .views import all_issues, get_detail, create_issue, my_issues, edit_issue


urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^my_issues$', my_issues, name='my_issues'),
    url(r'^edit/(?P<pk>\d+)$', edit_issue, name='edit'),
    url(r'^new$', create_issue, name='new_issue'),
    url(r'^(?P<pk>\d+)/$', get_detail, name='get_detail'),
]