from django.apps import AppConfig
# from django.db.models.signals import post_save	
# from .signals import greeting
# from .models import UpdateLinks


class ELibConfig(AppConfig):
    name = 'e_lib'

    def ready(self):
    	from e_lib import signals
