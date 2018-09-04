from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Comment
from .forms import IssueForm

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
    
def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(all_issues)
    else:
        form = IssueForm()
    return render(request, 'issueform.html', {'form': form})
    