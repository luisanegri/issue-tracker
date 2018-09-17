from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Comment
from .forms import IssueForm, CommentForm


def my_issues(request):
    user = request.user.id
    issues = Issue.objects.filter(created_by=user)
    return render(request, "myissues.html", {'issues': issues})
    
    
def all_issues(request):
    issues = Issue.objects.all()
    return render(request, 'issues.html', {'issues': issues})


def get_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.all()
    print(issue.comments)
    return render(request, 'detail.html', {'issue': issue}, {'comments': comments})
 
   
def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            return redirect('my_issues')
    else:
        form = IssueForm()
    return render(request, 'issueform.html', {'form': form})
   
def edit_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect(all_issues)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issueform.html', {'form': form})

    
def create_comment(request, pk):
    comments = Comment.objects.all()
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.issue = issue
            form.save()
            return redirect('get_detail', pk=issue.pk)
    else:
        form = CommentForm()

    return render(request, 'commentform.html', {'form': form, 'comments': comments})



