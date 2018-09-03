from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Product
class Issue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_do = models.BooleanField(blank=False, default=True)
    done = models.BooleanField(blank=False, default=False)
    doing = models.BooleanField(blank=False, default=False)
    user = models.ForeignKey(User,related_name='user_issue', on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

# Gives the user the ability to comment on issues
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True)
    # ForeignKey links to User and Issues models
    user = models.ForeignKey(User, related_name='user_comment')
    issue = models.ForeignKey(Issue, related_name='issue_comment')

    def __str__(self):
        return self.comment