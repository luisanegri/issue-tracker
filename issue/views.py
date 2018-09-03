from django.shortcuts import render, get_object_or_404
from .models import Issue, Comment

# Create your views here.
def all_issues(request):
    # Get all issues in the database
    issues = Issue.objects.all()
    return render(request, 'issues.html', {'issues': issues})
    
def get_detail(request, pk):
    # Get specific issue
    issue = get_object_or_404(Issue, pk=pk)
    # Filters comments in the database of specific issue
    comments = Comment.objects.filter(issue=pk)
    return render(request, 'detail.html', {'issue': issue}, {'comments': comments})
    