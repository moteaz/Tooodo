from django.urls import path
from .jwt_views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
)
from .views import (
    RegisterView,
    LoginView,
    TodoListCreateView,
    TodoDetailView,
)

urlpatterns = [
    # Authentication endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # Todo endpoints
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]