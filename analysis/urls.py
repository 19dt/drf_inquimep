from django.urls import path, include

from mainapp.views import (
    AnalisysGoldListAPIView, AnalysisGoldCreateAPIView, AnalisysSilverListAPIView, AnalysisSilverCreateAPIView,
)
urlpatterns = [
    path('analysis_gold/list', AnalisysGoldListAPIView.as_view(), name='analysis_gold_list'),
    path('analysis_gold/create', AnalysisGoldCreateAPIView.as_view(), name='analysis_gold_create'),
    path('analysis_silver/list', AnalisysSilverListAPIView.as_view(), name='analysis_silver_list'),
    path('analysis_silver/create', AnalysisSilverCreateAPIView.as_view(), name='analysis_silver_create'),
]