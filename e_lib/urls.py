from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('/<str:info>', views.folders, name='folders'),
    path('update', views.update, name='update')
]

