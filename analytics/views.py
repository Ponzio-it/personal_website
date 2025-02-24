from datetime import date, timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.views import View
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
    Allow GET and POST for everyone.
    Restrict PUT, PATCH, DELETE to admins only.
    """

    def has_permission(self, request, view):
        # If it's GET or POST, allow everyone
        if request.method in ['GET', 'POST']:
            return True
        
        # Else (PUT, PATCH, DELETE, etc.), require admin/staff
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

    def get_today_metric(self):
        """
        Retrieve or create the BusinessPerformanceMetric record for today's date.
        Returns (metric_instance, created_boolean).
        """
        today = date.today()
        metric, created = BusinessPerformanceMetric.objects.get_or_create(
            date=today,
            defaults={
                # Provide any defaults needed for new records
                'average_time_on_portfolio': timedelta(seconds=0),
                'ctr_contact_button': 0.0,
            }
        )
        return metric, created

    def create(self, request, *args, **kwargs):
        """
        Overrides default create() to increment total_views in today's record.
        If today's record does not exist, create a new one.
        """
        metric, created = self.get_today_metric()

        # Read the event_type from request data
        event_type = request.data.get('event_type', 'page_view')

        if event_type == 'contact_click':
            # Increment Contact CTR
            metric.ctr_contact_button += 1
        else:
            # Default is page_view or unknown event => increment total_views
            metric.total_views += 1
        
        metric.save()

        serializer = self.get_serializer(metric)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
        )
    
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

class AnalyticsPageView(View):
    """
    A class-based view for rendering the analytics page template.
    """

    template_name = "analytics/analytics.html"

    def get(self, request):
        """
        Renders the analytics page template.
        """
        context = {}
        return render(request, self.template_name, context)