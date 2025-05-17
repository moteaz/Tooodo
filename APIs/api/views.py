from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from todos.models import Todo
from .serializers import UserSerializer, TodoSerializer
from .permissions import IsOwner


class RegisterView(generics.CreateAPIView):
    """View for registering new users"""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []  # Explicitly empty to override default authentication
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """View for user login - returns JWT tokens"""
    
    permission_classes = [permissions.AllowAny]
    authentication_classes = []  # Explicitly empty to override default authentication
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class TodoListCreateView(generics.ListCreateAPIView):
    """View for listing and creating todos"""
    
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        # Return only todos owned by the current user
        return Todo.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        # Set the owner to the current user
        serializer.save(owner=self.request.user)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating and deleting a todo"""
    
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        # Return only todos owned by the current user
        return Todo.objects.filter(owner=self.request.user)