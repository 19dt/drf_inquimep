from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import status
from rest_framework import permissions
from .models import Client, Entry
from analysis.models import Analysis, Silver, Gold
from .serializers import ClientSerializer, EntrySerializer, AnalysisSerializer, AnalysisGoldSerializer, AnalysisSilverSerializer



# Create your views here.
class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    
class EntryListAPIView(ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
class EntryCreateAPIView(CreateAPIView):
    serializer_class = EntrySerializer
    
class AnalisysGoldListAPIView(ListAPIView):
    queryset = Gold.objects.all()
    serializer_class = AnalysisGoldSerializer
    
class AnalysisGoldCreateAPIView(CreateAPIView):
    serializer_class = AnalysisGoldSerializer
    
class AnalisysSilverListAPIView(ListAPIView):
    queryset = Silver.objects.all()
    serializer_class = AnalysisSilverSerializer
    
class AnalysisSilverCreateAPIView(CreateAPIView):
    serializer_class = AnalysisSilverSerializer
    
    

    
    

