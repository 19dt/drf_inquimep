from django.urls import path, include

from .views import *

urlpatterns = [
    path('user/list/', UserListAPIView.as_view(), name='user_list'),
    path('user/create/',UserCreateAPIView.as_view(), name='user_create'),
    path('user/update/<int:pk>',UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>',UserDestroyAPIView.as_view(), name='user_delete'),
    path('client/list/', ClientListAPIView.as_view(), name='client_list'),
    path('client/', ClientAPIView.as_view(), name='client'),
    path('client/create/',ClientCreateAPIView.as_view(), name='client_create'),
    path('client/update/<int:pk>',ClientUpdateAPIView.as_view(), name='client_update'),
    path('client/delete/<int:pk>',ClientDestroyAPIView.as_view(), name='client_delete'),
    path('entry/list/', EntryListAPIView.as_view(), name='entry_list'),
    path('entry/create/', EntryCreateAPIView.as_view(), name='entry_create'),
    path('entry/update/<int:pk>',EntryUpdateAPIView.as_view(), name='entry_update'),
    path('entry/delete/<int:pk>',EntryDestroyAPIView.as_view(), name='entry_delete'),
]