from django.urls import path
from .views import  ClienteView
 
urlpatterns=[
    path('clientes/', ClienteView.as_view(), name='companies_list'),
    path('clientes/<int:id>', ClienteView.as_view(), name='cliente_process')
]
