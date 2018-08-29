from django.conf.urls import url, include
from .views import all_issues


urlpatterns = [
    url(r'^$', all_issues, name='issues'),
]