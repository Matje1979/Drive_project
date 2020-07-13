from __future__ import print_function

from django.db import models
from django.db.models.signals import post_save, pre_save

import os.path
import sys
import codecs
#from apiclient import errors
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import re, time
import ast 
from django.db.models.signals import post_save


# Create your models here.


# class Folder(models.Model):
#   Name=models.CharField(max_length=100)
#   Folder_id=models.CharField(max_length=100)

#   def __str__(self):
#       return self.Name

class Book(models.Model):
    Book_id = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=60)
    Link = models.CharField(max_length=100, null = True, blank = True)
    Folder_id = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class UpdateLinks(models.Model):
    title = models.CharField(max_length = 50)
    Main_folder_id = models.CharField(max_length = 100, null=True, blank=True)

    def __str__(self):
        return self.title

# def greeting(sender, instance, **kwargs):
#     print ("Hello")



# post_save.connect(greeting, sender = UpdateLinks)


class Message(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Link = models.CharField(max_length = 100, null=True, blank=True)
    Text = models.TextField()

    def __str__(self):
        return self.Name

    







        

           