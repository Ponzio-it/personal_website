from django.test import TestCase
from ..models import (
    BusinessPerformanceMetric,
    EngagementMetric,
    ActiveSession,
    LoginAttempt,
    SystemHealthIndicator
)
from ..serializers import (
    BusinessPerformanceMetricSerializer,
    EngagementMetricSerializer,
    ActiveSessionSerializer,
    LoginAttemptSerializer,
    SystemHealthIndicatorSerializer
)
from datetime import timedelta, datetime
from django.utils.timezone import make_aware, now, localtime
import pytz

class SerializerTestCase(TestCase):
    def test_business_performance_metric_serializer(self):
        """Test serialization of BusinessPerformanceMetric model."""
        metric = BusinessPerformanceMetric.objects.create(
            total_views=100,
            unique_visitors=50,
            average_time_on_portfolio=timedelta(minutes=3),
            ctr_contact_button=5.5,
        )
        serializer = BusinessPerformanceMetricSerializer(metric)
        expected_data = {
            'total_views': 100,
            'unique_visitors': 50,
            'average_time_on_portfolio': "00:03:00",  # DurationField serializes to string
            'ctr_contact_button': 5.5,
            'date': metric.date.isoformat(),
        }
        self.assertEqual(serializer.data, expected_data)

    def test_engagement_metric_serializer(self):
        """Test serialization of EngagementMetric model."""
        metric = EngagementMetric.objects.create(
            user_sessions=200,
            pages_per_session=4.5,
            bounce_rate=65.0,
            active_users=10,
            top_pages_visited={"Home": 150, "About": 50},
        )
        serializer = EngagementMetricSerializer(metric)
        expected_data = {
            'user_sessions': 200,
            'pages_per_session': 4.5,
            'bounce_rate': 65.0,
            'active_users': 10,
            'top_pages_visited': {"Home": 150, "About": 50},
            'date': metric.date.isoformat(),
        }
        self.assertEqual(serializer.data, expected_data)

    def test_active_session_serializer(self):
        """Test serialization of ActiveSession model."""
        session = ActiveSession.objects.create(
            session_id="session123",
            user="test_user",
            start_time=make_aware(datetime(2025, 1, 8, 10, 0)),
            last_activity=make_aware(datetime(2025, 1, 8, 11, 0)),
        )
        serializer = ActiveSessionSerializer(session)
        expected_data = {
            'session_id': "session123",
            'user': "test_user",
            'start_time': session.start_time.isoformat(),
            'last_activity': session.last_activity.isoformat(),
        }
        self.assertEqual(serializer.data, expected_data)

    def test_login_attempt_serializer(self):
        """Test serialization of LoginAttempt model."""
        timestamp = localtime(now())

        login_attempt = LoginAttempt.objects.create(
            user="test_user",
            success=True,
            ip_address="127.0.0.1",
            timestamp=timestamp,
        )
        serializer = LoginAttemptSerializer(login_attempt)
        expected_data = {
            'user': "test_user",
            'timestamp': localtime(login_attempt.timestamp).isoformat(),
            'success': True,
            'ip_address': "127.0.0.1",
        }
        self.assertEqual(serializer.data, expected_data)

    def test_system_health_indicator_serializer(self):
        """Test serialization of SystemHealthIndicator model."""

        last_checked = localtime(now())

        health_indicator = SystemHealthIndicator.objects.create(
            status="Operational",
            errors_logged=0,
            uptime_percentage=99.9,
            last_checked=last_checked,
        )
        serializer = SystemHealthIndicatorSerializer(health_indicator)
        expected_data = {
            'status': "Operational",
            'last_checked': localtime(health_indicator.last_checked).isoformat(),
            'errors_logged': 0,
            'uptime_percentage': 99.9,
        }
        self.assertAlmostEqual(serializer.data, expected_data)
