from rest_framework import serializers
from .models import User, WasteCollector, WasteRecycler

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = "__all__"

class WasteCollectorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        password = attrs['password']
        return attrs
    
    class Meta:
        model = WasteCollector
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phonenumber', 'location', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(is_wastecollector=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wastecollector = WasteCollector.objects.create(user=user, **validated_data)
        return wastecollector

class WasteRecyclerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, attrs):
        password = attrs['password']
        # Validation logic for password
        return attrs
    
    class Meta:
        model = WasteRecycler
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phonenumber', 'password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(is_wasterecycler=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wasterecycler = WasteRecycler.objects.create(user=user, **validated_data)
        return wasterecycler
