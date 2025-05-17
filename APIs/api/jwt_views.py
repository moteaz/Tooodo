from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token view with AllowAny permission"""
    permission_classes = [AllowAny]
    authentication_classes = []


class CustomTokenRefreshView(TokenRefreshView):
    """Custom token refresh view with AllowAny permission"""
    permission_classes = [AllowAny]
    authentication_classes = []