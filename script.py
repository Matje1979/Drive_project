import os
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drive_app.settings')

# django.setup()

from e_lib.models import UpdateLinks
from django.db.models.signals import post_save

def greeting(sender, instance, created, **kwargs):
        print ("Hello World")

post_save.connect(greeting, sender = UpdateLinks)


print ("Hello")


# new_link = UpdateLinks(title = 'New_link')
# new_link.save()