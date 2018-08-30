from django.conf.urls import url, include
from .views import all_issues, get_detail


urlpatterns = [
    url(r'^$', all_issues, name='issues'),
    url(r'^(?P<pk>\d+)/$', get_detail, name='get_detail'),
]