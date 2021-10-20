from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('management/',views.ManageStock.as_view(),name='manage'),
    path('add-new-stock/',views.Addnewstock.as_view(),name='addnewstock'),
    path('edit-stock/<int:pk>/',views.UpdateProduct.as_view(),name='editstock')
]
