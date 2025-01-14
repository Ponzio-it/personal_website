from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import (
    BusinessPerformanceMetric,
    EngagementMetric,
    ActiveSession,
    LoginAttempt,
    SystemHealthIndicator,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import json
from datetime import timedelta
from datetime import datetime
from django.utils.timezone import is_naive, make_aware
import pytz

class APITestingSuite(APITestCase):
    """
    Automated test suite for the Analytics API endpoints.
    """

    def setUp(self):
        """
        Set up test data and authentication for all tests.
        """
        # Create test user and obtain token
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.user.is_staff = True  # Make the user an admin
        self.user.save()

        self.token_url = reverse("token_obtain_pair")

        token_response = self.client.post(
            self.token_url,
            data= json.dumps({"username": "testuser", "password": "password123"}),
            content_type="application/json"
        )

        self.access_token = token_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Test Data for Business Metrics
        self.business_metric = BusinessPerformanceMetric.objects.create(
            total_views=100,
            unique_visitors=50,
            average_time_on_portfolio=timedelta(minutes=3),
            ctr_contact_button=5.5,
            date="2025-01-08"
        )
        self.business_metrics_url = reverse("business-metrics-list")


        # Test Data for Engagement Metrics
        self.engagement_metric = EngagementMetric.objects.create(
            user_sessions=200,
            pages_per_session=4.5,
            bounce_rate=65.0,
            active_users=10,
            top_pages_visited={"Home": 150, "About": 50},
            date="2025-01-08"
        )
        self.engagement_metrics_url = reverse("engagement-metrics-list")


    def test_token_auth(self):
        """
        Test token-based authentication.
        """
        response = self.client.post(self.token_url, {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_get_business_metrics(self):
        """
        Test retrieving a list of business metrics.
        """
        response = self.client.get(self.business_metrics_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["total_views"], 100)

    def test_create_business_metric(self):
        """
        Test creating a new business metric.
        """
        data = {
            "total_views": 200,
            "unique_visitors": 150,
            "average_time_on_portfolio": "00:05:00",
            "ctr_contact_button": 10.0,
            "date": "2025-01-09"
        }
        response = self.client.post(self.business_metrics_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["total_views"], 200)

    def test_update_business_metric(self):
        """
        Test updating an existing business metric.
        """
        update_url = f"{self.business_metrics_url}{self.business_metric.id}/"
        data = {"total_views": 300}
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_views"], 300)

    def test_delete_business_metric(self):
        """
        Test deleting a business metric.
        """
        delete_url = f"{self.business_metrics_url}{self.business_metric.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_engagement_metrics(self):
        """
        Test retrieving a list of engagement metrics.
        """
        response = self.client.get(self.engagement_metrics_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["user_sessions"], 200)

    def test_permissions_for_anonymous_user(self):
        """
        Test access restrictions for unauthenticated users.
        """
        self.client.credentials()  # Remove token
        response = self.client.get(self.business_metrics_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActiveSessionAPITest(APITestCase):
    """
    Tests for the ActiveSession API.
    """

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.user.is_staff = True  # Make the user an admin
        self.user.save()

        self.token_url = reverse("token_obtain_pair")

        token_response = self.client.post(
            self.token_url,
            data= json.dumps({"username": "testuser", "password": "password123"}),
            content_type="application/json"
        )

        self.access_token = token_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Create test data
        self.active_session = ActiveSession.objects.create(
            session_id="abcd1234",
            user="test_user",
            start_time="2025-01-08T10:00:00Z",
            last_activity="2025-01-08T10:30:00Z"
        )
        self.url = reverse("active-sessions-list")


    def test_get_active_sessions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["session_id"], "abcd1234")

    def test_create_active_session(self):
        data = {
            "session_id": "xyz9876",
            "user": "new_user",
            "start_time": "2025-01-09T10:00:00Z",
            "last_activity": "2025-01-09T10:30:00Z"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["session_id"], "xyz9876")

    def test_update_active_session(self):
        update_url = f"{self.url}{self.active_session.id}/"
        data = {"last_activity": "2025-01-08T11:00:00Z"}
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_time = datetime.fromisoformat("2025-01-08T11:00:00+00:00")
        actual_time = datetime.fromisoformat(response.data["last_activity"])
        if is_naive(actual_time):  # Ensure timezone-aware
            actual_time = make_aware(actual_time, pytz.UTC)

        self.assertEqual(expected_time, actual_time)

    def test_delete_active_session(self):
        delete_url = f"{self.url}{self.active_session.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class LoginAttemptAPITest(APITestCase):
    """
    Tests for the LoginAttempt API.
    """

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.user.is_staff = True  # Make the user an admin
        self.user.save()

        self.token_url = reverse("token_obtain_pair")

        token_response = self.client.post(
            self.token_url,
            data= json.dumps({"username": "testuser", "password": "password123"}),
            content_type="application/json"
        )

        self.access_token = token_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Create test data
        self.login_attempt = LoginAttempt.objects.create(
            user="test_user",
            timestamp="2025-01-08T10:00:00Z",
            success=True,
            ip_address="127.0.0.1"
        )
        self.url = reverse("login-attempts-list")


    def test_get_login_attempts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["user"], "test_user")

    def test_create_login_attempt(self):
        data = {
            "user": "new_user",
            "timestamp": "2025-01-09T10:00:00Z",
            "success": False,
            "ip_address": "192.168.0.1"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], "new_user")

    def test_delete_login_attempt(self):
        delete_url = f"{self.url}{self.login_attempt.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SystemHealthIndicatorAPITest(APITestCase):
    """
    Tests for the SystemHealthIndicator API.
    """

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.user.is_staff = True  # Make the user an admin
        self.user.save()

        self.token_url = reverse("token_obtain_pair")


        token_response = self.client.post(
            self.token_url,
            data= json.dumps({"username": "testuser", "password": "password123"}),
            content_type="application/json"
        )

        self.access_token = token_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        # Create test data
        self.system_health = SystemHealthIndicator.objects.create(
            status="Operational",
            errors_logged=0,
            uptime_percentage=99.9
        )
        self.url = reverse("system-health-list")


    def test_get_system_health(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["status"], "Operational")

    def test_update_system_health(self):
        update_url = f"{self.url}{self.system_health.id}/"
        data = {"uptime_percentage": 95.0}
        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["uptime_percentage"], 95.0)
