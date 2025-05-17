from rest_framework import serializers
from django.contrib.auth.models import User
from todos.models import Todo


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class TodoSerializer(serializers.ModelSerializer):
    """Serializer for the Todo model"""
    
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'status', 'owner', 
                  'created_at', 'updated_at', 'due_date')
        read_only_fields = ('id', 'created_at', 'updated_at', 'owner')