from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

import os

# Create your models here.

class Projects(models.Model):
    proj_name = models.CharField(max_length=50,unique=True)
    user_team = models.ManyToManyField(User,related_name='projects') # multiple users can be involved in multiple proj teams
    wiki = RichTextUploadingField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proj_name


class Issues(models.Model):
    ### media upload pending . . 
    project = models.ForeignKey(Projects,related_name='issues',on_delete=models.CASCADE) # each project can have multiple issues
    heading = models.CharField(max_length=50)
    description = RichTextUploadingField()
    composer = models.ForeignKey(User, related_name='issue_user',null=True, on_delete=models.SET_NULL) # each user can create multiple issues
    
    PRIORITY = (
        ('low','low'),
        ('medium','medium'),
        ('high','high'),
    )
    priority = models.CharField(max_length=50,null=True,choices=PRIORITY)
    
    TAGS = (
        ('logical','logical'),
        ('functional','functional'),
        ('performance','performance'),
        ('security','security'),
        ('bug','bug'),
        ('frontend','frontend'),
        ('guideline','guideline'),
        ('naming','naming'),
    )
    tags = models.CharField(max_length = 50,null=True,choices=TAGS)

    STATUS = (
        ('pending','pending'),
        ('to be discussed ','to be discussed '),
        ('resolved','resolved'),
        ('in review','in review'),
    )
    status = models.CharField(max_length=50,null=True,choices=STATUS)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading