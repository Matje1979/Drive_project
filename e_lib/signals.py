#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import django
from django.conf import settings

import os.path
import codecs

#from apiclient import errors
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import re, time
import ast 
from django.db.models.signals import post_save
from .models import UpdateLinks, Book
from django.dispatch import receiver



save_to_path = '/home/damir/drive_app/e_lib/CicaGoran/results'

#determining what information will the app try to access.
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

#this is where the tokens received from the api will be stored.
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)

DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))


def make_html_name(folder_name):
    folder_name_striped = folder_name.strip()
    folder_name_list = folder_name_striped.split()
    folder_name_joined = '_'.join(folder_name_list)
    to_file = folder_name_joined + ".html"
    return to_file

def make_html_link_name(folder_name):
    folder_name_striped = folder_name.strip()
    folder_name_list = folder_name_striped.split()
    folder_name_joined = '_'.join(folder_name_list)
    to_file = folder_name_joined + ".html"
    return to_file

def elim_ext(c):
    #eliminating the file extension with regular expressions 
    pattern = re.compile(r'\.\w+\b')  # creating a pattern.
    b = ''
    for f in c:
        match = pattern.search(f['name']) # searching for a match.
        if match is not None:
            a = f['name'].replace(match.group(), b) # creating a new string
            f['name'] = a # replacing the value of the key with the new string.
    return c

def get_folder_data(folder_id):
    page_token = None
    c = []
    d = []
    count = 0
    check = 0
    while True:
    #parameters to the list function determine what data in the given scope will be retrieved.
        files = DRIVE.files().list(q="'{}' in parents".format(folder_id), pageSize = 100, fields = 'nextPageToken, files(name, webViewLink, id, mimeType)',
            pageToken = page_token).execute()

        for file in files.get('files', []):
          
            if file['mimeType'] == 'application/vnd.google-apps.folder':
            
                del file['webViewLink']
                file['folder_id'] = folder_id
                d.append(file)
                d += get_folder_data(file['id'])#this recursive function is called the number of times equal to the number of folders.
                check += 1

            else:
                file['folder_id'] = folder_id
                c.append(file) #files are put into separate list because the need to be bellow the folders if they are on the same page.
                count += 1

        page_token = files.get('nextPageToken', None)
        if page_token is None:
            break
    e = elim_ext(c)
    
    d = elim_ext(d)
   
    h = d + e #the goes first because folders should be on top of the page
    return h
    

@receiver(post_save, sender = UpdateLinks)
def getLinks(sender, instance, **kwargs):
    
    folder_id = instance.Main_folder_id

    data_list = get_folder_data(folder_id)

    for item in data_list:
        try:
            Book.objects.create(Name = item['name'], Link = item['webViewLink'], Folder_id = item['id'])
        except KeyError:
            Book.objects.create(Name = item['name'], Folder_id = item['id'])

    to_file = 'data_list.txt'
    complete_name = os.path.join(save_to_path, to_file)
    with open(complete_name, 'w') as f:
            f.write(str(data_list))







        

           