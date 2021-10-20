from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('management',views.manage,name='manage'),
    path('edit-stock',views.editstock,name='editstock'),
]
