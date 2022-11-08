from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name= 'index'),
    path('category/<int:category_id>', views.category, name='category'),
    
    
]

