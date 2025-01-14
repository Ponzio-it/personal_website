from rest_framework import serializers
from .models import BusinessPerformanceMetric, EngagementMetric, ActiveSession, LoginAttempt, SystemHealthIndicator

class BusinessPerformanceMetricSerializer(serializers.ModelSerializer):
    """
    Serializer for the Business Performance Metric model.
    Converts model data to JSON for API responses and ensures security.
    """
    class Meta:
        model = BusinessPerformanceMetric
        fields = ['total_views', 'unique_visitors', 'average_time_on_portfolio', 'ctr_contact_button', 'date']


class EngagementMetricSerializer(serializers.ModelSerializer):
    """
    Serializer for Engagement Metric model.
    Handles JSONField for top_pages_visited cleanly.
    """
    class Meta:
        model = EngagementMetric
        fields = ['user_sessions', 'pages_per_session', 'bounce_rate', 'active_users', 'top_pages_visited', 'date']

class ActiveSessionSerializer(serializers.ModelSerializer):
    """
    Serializer for Active Session model.
    Exposes session-related data for frontend monitoring.
    """
    class Meta:
        model = ActiveSession
        fields = ['session_id', 'user', 'start_time', 'last_activity']

class LoginAttemptSerializer(serializers.ModelSerializer):
    """
    Serializer for Login Attempt model.
    Captures key data for security auditing.
    """
    class Meta:
        model = LoginAttempt
        fields = ['user', 'timestamp', 'success', 'ip_address']

class SystemHealthIndicatorSerializer(serializers.ModelSerializer):
    """
    Serializer for System Health Indicator model.
    Exposes high-level system metrics for frontend display.
    """
    class Meta:
        model = SystemHealthIndicator
        fields = ['status', 'last_checked', 'errors_logged', 'uptime_percentage']