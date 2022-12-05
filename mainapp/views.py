from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework import permissions
from .models import Client, Entry, User
from analysis.models import Analysis, Silver, Gold
from .serializers import ClientSerializer, EntrySerializer, AnalysisSerializer, AnalysisGoldSerializer, AnalysisSilverSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

# Login / Logout

class Login(FormView):
    template_name: "login.html"
    form_class: AuthenticationForm
    success_url: reverse_lazy('user:user_list')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(self,*args,**kwargs)
    
    def form_valid(self, form):
        user = authenticate()
    

# Métodos APIVIEW.

class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer

class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class ClientDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el cliente {self.kwargs['pk']}"})
    
class EntryListAPIView(ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
class EntryCreateAPIView(CreateAPIView):
    serializer_class = EntrySerializer
    
class EntryUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class EntryDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente la entrada {self.kwargs['pk']}"})
    
class AnalisysGoldListAPIView(ListAPIView):
    queryset = Gold.objects.all()
    serializer_class = AnalysisGoldSerializer
    
class AnalysisGoldCreateAPIView(CreateAPIView):
    serializer_class = AnalysisGoldSerializer
    
class AnalysisGoldUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AnalysisGoldDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el analisis oro {self.kwargs['pk']}"})
    
class AnalisysSilverListAPIView(ListAPIView):
    queryset = Silver.objects.all()
    serializer_class = AnalysisSilverSerializer
    
class AnalysisSilverCreateAPIView(CreateAPIView):
    serializer_class = AnalysisSilverSerializer
    
class AnalysisSilverUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class AnalysisSilverDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el analisis plata {self.kwargs['pk']}"})
    

# Modificando APIView

class ClientAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(self.request.query_params)
        return Response({'resp': True})
    
    def post(self, request, *args, **kwargs):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many = True)
        return Response(serializer.data)