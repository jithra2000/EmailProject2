from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.addDetails,name='addDetails'),
    path('table',views.table,name='table'),
    path('data',views.data,name='data'),
    path('delete/<int:pk>',views.delete,name='delete')
    
]