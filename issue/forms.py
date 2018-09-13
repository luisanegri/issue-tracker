from django import forms
from .models import Issue, Comment

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('name', 'description', 'varieties')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)