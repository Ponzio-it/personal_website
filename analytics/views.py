from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    BusinessPerformanceMetric,
    EngagementMetric,
    ActiveSession,
    LoginAttempt,
    SystemHealthIndicator,
)
from .serializers import (
    BusinessPerformanceMetricSerializer,
    EngagementMetricSerializer,
    ActiveSessionSerializer,
    LoginAttemptSerializer,
    SystemHealthIndicatorSerializer,
)

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to modify data, but read access for others.
    """

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True  # Allow read-only access
        return request.user and request.user.is_staff



class BusinessPerformanceMetricViewSet(ModelViewSet):
    """
    API endpoint for Business Performance Metrics.
    Provides list, retrieve, create, update, and delete functionality.
    ViewSet for Business Performance Metrics with filtering, search, and ordering.
    """
    queryset = BusinessPerformanceMetric.objects.all()
    serializer_class = BusinessPerformanceMetricSerializer
    permission_classes = [IsAdminOrReadOnly]
     # Add filtering and search
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date']  # Filter by specific fields
    search_fields = ['total_views', 'unique_visitors']  # Search on specific fields
    ordering_fields = ['date', 'total_views', 'unique_visitors']  # Allow ordering

class EngagementMetricViewSet(ModelViewSet):
    """
    ViewSet for Engagement Metrics with filtering, search, and ordering.
    """
    queryset = EngagementMetric.objects.all()
    serializer_class = EngagementMetricSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['date']
    search_fields = ['user_sessions', 'pages_per_session', 'active_users']
    ordering_fields = ['date', 'user_sessions', 'bounce_rate']

class ActiveSessionViewSet(ModelViewSet):
    """
    ViewSet for Active Sessions with filtering and ordering.
    """
    queryset = ActiveSession.objects.all()
    serializer_class = ActiveSessionSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user']
    search_fields = ['user', 'session_id']
    ordering_fields = ['start_time', 'last_activity']

class LoginAttemptViewSet(ModelViewSet):
    """
    ViewSet for Login Attempts with filtering and search.
    """
    queryset = LoginAttempt.objects.all()
    serializer_class = LoginAttemptSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['success', 'ip_address']  # Filter by success or IP
    search_fields = ['user', 'ip_address']
    ordering_fields = ['timestamp']

class SystemHealthIndicatorViewSet(ModelViewSet):
    """
    ViewSet for System Health Indicators with filtering and ordering.
    """
    queryset = SystemHealthIndicator.objects.all()
    serializer_class = SystemHealthIndicatorSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['last_checked', 'uptime_percentage']