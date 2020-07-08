# -*- coding: utf-8 -*-
# import sys, os
# from drive_app import settings 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drive_app.settings")
# django.setup()

def sort_f(c, name):

    name = name
    #sorting the files' metadata according to the alpahbetic order of the file names.
    d = []
    for f in c:
        # print (f)
        d.append(f[name].upper())
    g = sorted(d)

    # checking for duplicate items.
    #print ("List count:", len(g))
    f = set(g)
    #print ("Set count:", len(f))

    # adding urls to file names
    e = []
    count = 0
    for item in g:
        for f in c:
            if item == f[name].upper():
                e.append(f)
                i = c.index(f)
                del c[i]
                count +=1
                break  #stops loop after first match is found (necessary because there may be repeated items)
    return e