from rest_framework import serializers
from .models import User, Client, Entry
from analysis.models import Analysis, Gold, Silver

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name','password1', 'password2', 'is_staff')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
    
    def to_representation(self, instance):
        return instance.toJSON()
    
class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class AnalysisGoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = '__all__'

class AnalysisSilverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Silver
        fields = '__all__'
        
        