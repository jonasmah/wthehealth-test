from django.conf import settings

def google_analytics(request):
    return {
        'GA_TRACKING_ID': 'G-T9DPDVJD01'  # Your GA4 measurement ID
    }