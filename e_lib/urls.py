from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update', views.update, name='update'),
    path('<str:parent_id>', views.getBooks, name='getBooks'),
    path('results/', views.searchResults, name='results'),  
    path('kontakt/', views.kontakt, name='kontakt'),
    path('o_nama/', views.o_nama, name='o_nama'),
	path('statistika/', views.statistika, name='statistika')  
]

