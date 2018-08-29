from django.shortcuts import render
from .models import Issue

# Create your views here.
def all_issues(request):
    issues = Issue.objects.all()
    return render(request, 'issues.html', {'issues': issues})