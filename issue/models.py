from django.db import models
from django.contrib.auth.models import User

# Product
class Issue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='user_issue', on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name

    class Varieties(models.Model):
        BUG = 'Bug'
        FEATURE = 'Feature'
  
        VARIETIES_CHOICES = (
            (BUG, 'Bug'),
            (FEATURE, 'Feature'),
        )
        varieties = models.CharField(
            max_length=40,
            choices=VARIETIES_CHOICES,
            default=BUG,
        )
    
        def __str__(self):
            return self.varieties

    class Status(models.Model):
        TODO = 'To do'
        DOING = 'Doing'
        DONE = 'Done'
  
        STATUS_CHOICES = (
            (TODO, 'To do'),
            (DOING, 'Doing'),
            (DONE, 'Done'),
        )
        status = models.CharField(
            max_length=40,
            choices=STATUS_CHOICES,
            default=TODO,
        )
    
        def __str__(self):
            return self.status


# Gives the user the ability to comment on issues
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKey links to User and Issues models
    user = models.ForeignKey(User, related_name='user_comment')
    issue = models.ForeignKey(Issue, related_name='issue_comment')

    def __str__(self):
        return self.comment