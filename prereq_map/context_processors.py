from django.conf import settings


def google_analytics(request):

    ga_key = getattr(settings, 'GOOGLE_ANALYTICS_KEY', False)
    return {
        'google_analytics': ga_key
    }
