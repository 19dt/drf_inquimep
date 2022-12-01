from django.urls import path, include

from mainapp.views import (
    AnalisysGoldListAPIView, AnalysisGoldCreateAPIView, AnalisysSilverListAPIView, AnalysisSilverCreateAPIView,
    AnalysisGoldUpdateAPIView, AnalysisGoldDestroyAPIView, AnalysisSilverUpdateAPIView, AnalysisSilverDestroyAPIView
)
urlpatterns = [
    path('analysis_gold/list/', AnalisysGoldListAPIView.as_view(), name='analysis_gold_list'),
    path('analysis_gold/create/', AnalysisGoldCreateAPIView.as_view(), name='analysis_gold_create'),
    path('analysis_gold/update/<int:pk>', AnalysisGoldUpdateAPIView.as_view(), name= 'analysis_gold_update'),
    path('analysis_gold/delete/<int:pk>', AnalysisGoldDestroyAPIView.as_view(), name= 'analysis_gold_delete'),
    path('analysis_silver/list/', AnalisysSilverListAPIView.as_view(), name='analysis_silver_list'),
    path('analysis_silver/create/', AnalysisSilverCreateAPIView.as_view(), name='analysis_silver_create'),
    path('analysis_silver/update/<int:pk>', AnalysisSilverUpdateAPIView.as_view(), name= 'analysis_silver_update'),
    path('analysis_silver/delete/<int:pk>', AnalysisSilverDestroyAPIView.as_view(), name= 'analysis_silver_delete'),
]