
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.feed, name='feed'),
    path('view/<int:pk>', views.View, name='view'),
    path('new', views.Create, name='new'),
    path('edit/<int:pk>', views.Update,  name='edit'),
    path('delete/<int:pk>', views.Delete , name='delete'),
]