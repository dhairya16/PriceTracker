from django.urls import path
from links import views

urlpatterns = [
    path('update/', views.udateLinks, name = 'update'),
    path('delete/<int:pk>', views.deleteLink, name = 'delete'),
    path('', views.home_view, name = 'home'),
]
