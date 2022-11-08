from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name="add"),
    path('delete/<int:product_id>/', views.delete, name="detele"),
    path('subtract/<int:product_id>/', views.subtract, name="subtract"),
    path('clear/', views.clear, name="clear"),
          
]
