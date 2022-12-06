from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status, viewsets
from .models import Client, Entry, User
from analysis.models import Analysis, Silver, Gold
from .serializers import ClientSerializer, EntrySerializer, AnalysisSerializer, AnalysisGoldSerializer, AnalysisSilverSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

# Login / Logout

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('mainapp:client_list')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)
    
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password= form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)   
        
class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK) 

# Métodos APIVIEW.

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User
    
    def delete(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=self.kwargs['pk'])
        instance.delete()
        return Response({'msg': f"Se ha eliminado correctamente el usuario {self.kwargs['pk']}"})

class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication, )
    
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
    

# ModelViewSet

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer