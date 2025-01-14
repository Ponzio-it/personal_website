from django.db import models
from django.utils.translation import gettext_lazy as _

class BusinessPerformanceMetric(models.Model):
    """
    Model representing metrics for the Business Performance Dashboard.
    Tracks overall portfolio visibility and key engagement indicators.
    """
    total_views = models.PositiveIntegerField(
        default=0,
        help_text=_("Total number of portfolio views."),
        verbose_name=_("Total Portfolio Views")
    )
    unique_visitors = models.PositiveIntegerField(
        default=0,
        help_text=_("Number of unique visitors to the portfolio."),
        verbose_name=_("Unique Visitors")
    )
    average_time_on_portfolio = models.DurationField(
        help_text=_("Average time spent by users on the portfolio."),
        verbose_name=_("Average Time on Portfolio")
    )
    ctr_contact_button = models.FloatField(
        default=0.0,
        help_text=_("Click-through rate (CTR) for the 'Send Message' button on the Contact Me page."),
        verbose_name=_("Contact Button CTR")
    )

    date = models.DateField(
        auto_now_add=True,
        help_text=_("Date for which the metrics are tracked."),
        verbose_name=_("Date")
    )

    def __str__(self):
        return f"Metrics for {self.date}"

    class Meta:
        verbose_name = _("Business Performance Metric")
        verbose_name_plural = _("Business Performance Metrics")


class EngagementMetric(models.Model):
    """
    Model representing metrics for the Engagement Dashboard.
    Tracks user activity and engagement behavior on the portfolio.
    """
    user_sessions = models.PositiveIntegerField(
        default=0,
        help_text=_("Total number of user sessions."),
        verbose_name=_("User Sessions")
    )
    pages_per_session = models.FloatField(
        default=0.0,
        help_text=_("Average number of pages viewed per session."),
        verbose_name=_("Pages Per Session")
    )
    bounce_rate = models.FloatField(
        default=0.0,
        help_text=_("Percentage of users who leave after viewing only one page."),
        verbose_name=_("Bounce Rate (%)")
    )
    active_users = models.PositiveIntegerField(
        default=0,
        help_text=_("Number of active users currently on the portfolio."),
        verbose_name=_("Active Users")
    )
    top_pages_visited = models.JSONField(
        default=dict,
        help_text=_("JSON data for top pages visited, e.g., {'Home': 150, 'About': 100}."),
        verbose_name=_("Top Pages Visited")
    )

    date = models.DateField(
        auto_now_add=True,
        help_text=_("Date for which the metrics are tracked."),
        verbose_name=_("Date")
    )

    def __str__(self):
        return f"Engagement Metrics for {self.date}"

    class Meta:
        verbose_name = _("Engagement Metric")
        verbose_name_plural = _("Engagement Metrics")

class ActiveSession(models.Model):
    """
    Model representing active sessions on the portfolio.
    Tracks session start and last activity time for security monitoring.
    """
    session_id = models.CharField(
        max_length=100,
        help_text=_("Unique identifier for the session."),
        verbose_name=_("Session ID")
    )
    user = models.CharField(
        max_length=100,
        help_text=_("Identifier for the user associated with the session."),
        verbose_name=_("User")
    )
    start_time = models.DateTimeField(
        help_text=_("Timestamp when the session started."),
        verbose_name=_("Session Start Time")
    )
    last_activity = models.DateTimeField(
        help_text=_("Timestamp of the last activity in this session."),
        verbose_name=_("Last Activity Time")
    )

    def __str__(self):
        return f"Session {self.session_id} - {self.user}"

    class Meta:
        verbose_name = _("Active Session")
        verbose_name_plural = _("Active Sessions")

class LoginAttempt(models.Model):
    """
    Model representing login attempt logs.
    Includes both successful and failed login attempts for security monitoring.
    """
    user = models.CharField(
        max_length=100,
        help_text=_("Identifier for the user attempting to log in."),
        verbose_name=_("User")
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Timestamp of the login attempt."),
        verbose_name=_("Timestamp")
    )
    success = models.BooleanField(
        default=False,
        help_text=_("Indicates whether the login attempt was successful."),
        verbose_name=_("Successful Attempt")
    )
    ip_address = models.GenericIPAddressField(
        help_text=_("IP address of the user attempting to log in."),
        verbose_name=_("IP Address")
    )

    def __str__(self):
        status = "Success" if self.success else "Failed"
        return f"{status} Login - {self.user} at {self.timestamp}"

    class Meta:
        verbose_name = _("Login Attempt")
        verbose_name_plural = _("Login Attempts")


class SystemHealthIndicator(models.Model):
    """
    Model representing the health status of the portfolio system.
    Tracks uptime, errors, and performance metrics.
    """
    status = models.CharField(
        max_length=50,
        choices=[('Operational', _("Operational")), ('Degraded', _("Degraded")), ('Down', _("Down"))],
        default='Operational',
        help_text=_("Overall health status of the system."),
        verbose_name=_("System Status")
    )
    last_checked = models.DateTimeField(
        auto_now=True,
        help_text=_("Timestamp of the last health check."),
        verbose_name=_("Last Checked")
    )
    errors_logged = models.PositiveIntegerField(
        default=0,
        help_text=_("Number of errors logged since the last health check."),
        verbose_name=_("Errors Logged")
    )
    uptime_percentage = models.FloatField(
        default=100.0,
        help_text=_("Percentage of uptime in the monitoring period."),
        verbose_name=_("Uptime Percentage")
    )

    def __str__(self):
        return f"System Status: {self.status} (Checked: {self.last_checked})"

    class Meta:
        verbose_name = _("System Health Indicator")
        verbose_name_plural = _("System Health Indicators")
