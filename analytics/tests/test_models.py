from django.test import TestCase
from analytics.models import BusinessPerformanceMetric, EngagementMetric, ActiveSession, LoginAttempt, SystemHealthIndicator
from django.utils.timezone import now
from datetime import timedelta

class BusinessPerformanceMetricTestCase(TestCase):
    """
    Test case for the BusinessPerformaceMetric model.
    Ensure proper creation and behaviour of fields like  total views,
    unique visitors.
    """
    
    def setUp(self):
        """
        Set up test data for BusinessPerformanceMetric
        """
        self.metric = BusinessPerformanceMetric.objects.create(
            total_views=100,
            unique_visitors=50,
            average_time_on_portfolio=timedelta(minutes=5, seconds=30),
            ctr_contact_button=2.5,
            date=now().date()
        )

    def test_metric_creation(self):
        """
         Verify that BusinessPerformanceMetric fields are correctly saved.
        """
        self.assertEqual(self.metric.total_views, 100)
        self.assertEqual(self.metric.unique_visitors, 50)
        self.assertEqual(self.metric.ctr_contact_button, 2.5)

    def test_average_time_format(self):
        """
        Verify that average_time_on_portfolio behaves as expected
        """
        self.assertEqual(str(self.metric.average_time_on_portfolio), '0:05:30')

class EngagementMetricTestCase(TestCase):
    """
    Test case for the EngagementMetric model.
    Ensures proper creation and behavior of fields like user sessions,
    bounce rate, and top pages visited.
    """

    def setUp(self):
        """
        Set up test data for EngagementMetric.
        """
        self.metric = EngagementMetric.objects.create(
            user_sessions=120,
            pages_per_session=4.5,
            bounce_rate=25.0,
            active_users=10,
            top_pages_visited={"Home": 50, "Portfolio": 30},
            date=now().date()
        )

    def test_metric_creation(self):
        """
        Verify that EngagementMetric fields are correctly saved.
        """
        self.assertEqual(self.metric.user_sessions, 120)
        self.assertEqual(self.metric.pages_per_session, 4.5)
        self.assertEqual(self.metric.bounce_rate, 25.0)
        self.assertEqual(self.metric.active_users, 10)

    def test_top_pages_visited(self):
        """
        Check that the top_pages_visited field behaves as expected.
        """
        self.assertEqual(self.metric.top_pages_visited['Home'], 50)
        self.assertEqual(self.metric.top_pages_visited['Portfolio'], 30)


class ActiveSessionTestCase(TestCase):
    """
    Test case for the ActiveSession model.
    Validates session creation and timestamp behavior.
    """

    def setUp(self):
        """
        Set up test data for ActiveSession.
        """
        self.session = ActiveSession.objects.create(
            session_id="abc123",
            user="test_user",
            start_time=now(),
            last_activity=now()
        )

    def test_session_creation(self):
        """
        Verify that ActiveSession fields are correctly saved.
        """
        self.assertEqual(self.session.session_id, "abc123")
        self.assertEqual(self.session.user, "test_user")

    def test_session_timestamps(self):
        """
        Ensure timestamps for start_time and last_activity are not null.
        """
        self.assertIsNotNone(self.session.start_time)
        self.assertIsNotNone(self.session.last_activity)

class LoginAttemptTestCase(TestCase):
    """
    Test case for the LoginAttempt model.
    Ensures proper creation and validation of login attempt logs.
    """

    def setUp(self):
        """
        Set up test data for LoginAttempt.
        """
        self.login_attempt = LoginAttempt.objects.create(
            user="test_user",
            success=False,
            ip_address="127.0.0.1",
            timestamp=now()
        )

    def test_login_attempt_creation(self):
        """
        Verify that LoginAttempt fields are correctly saved.
        """
        self.assertEqual(self.login_attempt.user, "test_user")
        self.assertEqual(self.login_attempt.success, False)
        self.assertEqual(self.login_attempt.ip_address, "127.0.0.1")

    def test_login_attempt_timestamp(self):
        """
        Ensure the timestamp field is not null.
        """
        self.assertIsNotNone(self.login_attempt.timestamp)

class SystemHealthIndicatorTestCase(TestCase):
    """
    Test case for the SystemHealthIndicator model.
    Validates creation and behavior of system health fields.
    """

    def setUp(self):
        """
        Set up test data for SystemHealthIndicator.
        """
        self.indicator = SystemHealthIndicator.objects.create(
            status="Operational",
            last_checked=now(),
            errors_logged=2,
            uptime_percentage=99.9
        )

    def test_health_indicator_creation(self):
        """
        Verify that SystemHealthIndicator fields are correctly saved.
        """
        self.assertEqual(self.indicator.status, "Operational")
        self.assertEqual(self.indicator.errors_logged, 2)
        self.assertEqual(self.indicator.uptime_percentage, 99.9)

    def test_last_checked_timestamp(self):
        """
        Ensure the last_checked timestamp field is not null.
        """
        self.assertIsNotNone(self.indicator.last_checked)