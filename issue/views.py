from django.shortcuts import render, get_object_or_404, redirect
from .models import Issue, Comment
from .forms import IssueForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required   
def my_issues(request):
    issues = Issue.objects.filter(created_by=request.user)
    return render(request, "myissues.html", {'issues': issues})
    
@login_required   
def all_issues(request):
    issues = Issue.objects.all().order_by('-upvotes')
    return render(request, 'issues.html', {'issues': issues})

@login_required   
def get_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    comments = Comment.objects.all()
    return render(request, 'detail.html', {'issue': issue}, {'comments': comments})
 
@login_required    
def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            messages.success(request, 'New issue created successfully!')
            return redirect('my_issues')
    else:
        form = IssueForm()
    return render(request, 'issueform.html', {'form': form})
    
@login_required      
def edit_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your issue was updated successfully!')
            return redirect(my_issues)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issueform.html', {'form': form})

def delete_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    issue.delete()
    return redirect(my_issues)

@login_required   
def upvote(request, pk):
    issue = Issue.objects.get(pk=pk)
    issue.upvotes += 1
    issue.save()
    messages.success(request, 'Upvoted successfully!')
    return redirect('get_detail', pk)

@login_required       
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


        
@login_required   
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('get_detail', pk=comment.issue.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'commentform.html', {'form': form})       


