from rest_framework import serializers
from .models import User, Client, Entry
from django.contrib.auth.models import User
from analysis.models import Analysis, Gold, Silver

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    fist_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('fist_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data
        


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
        
        