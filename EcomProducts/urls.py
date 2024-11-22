from django.contrib import admin
from django.urls import path  # remove render and redirect from here
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #new
from django.contrib.auth import views as authentication_views

app_name = 'ecomproducts'

urlpatterns = [
    path('create', views.create_item, name='create_Product'), 
    path('myproducts', views.item_list, name='all_Product'), 
    path('update/<int:pk>/', views.update_item, name='update_Product'),
    path('delete/<int:pk>/', views.delete_item, name='delete_Product'),
 

    


]