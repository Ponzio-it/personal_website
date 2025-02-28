// analytics.js
document.addEventListener('DOMContentLoaded', function() {
  // On each page load, increment today's total_views
  fetch('/en/analytics/api/business-metrics/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        event_type: 'page_view'
    })
  })

  .then(response => response.json())
  .then(data => {
    console.log('BusinessPerformanceMetric updated:', data);
  })
  .catch(error => {
    console.error('Error incrementing total_views:', error);
  });
});

// 2. Track "Contact Me" button clicks
  //    - Suppose your Contact Me button has an ID of #contact-button.
  const contactButton = document.getElementById('contact-button');
  if (contactButton) {
    contactButton.addEventListener('click', function() {
      fetch('/en/analytics/api/business-metrics/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event_type: 'contact_click'
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log('CTR incremented:', data);
      })
      .catch(error => {
        console.error('Error incrementing CTR:', error);
      });
    });
}

