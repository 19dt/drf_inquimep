from django.urls import path, include

from .views import (
    ClientListAPIView, EntryListAPIView, EntryCreateAPIView, ClientCreateAPIView, AnalisysGoldListAPIView, AnalysisGoldCreateAPIView, AnalisysSilverListAPIView, AnalysisSilverCreateAPIView,
)

urlpatterns = [
    path('client/list/', ClientListAPIView.as_view(), name='client_list'),
    path('client/create/',ClientCreateAPIView.as_view(), name='client_create'),
    path('entry/list/', EntryListAPIView.as_view(), name='entry_list'),
    path('entry/create/', EntryCreateAPIView.as_view(), name='entry_create'),
    
]