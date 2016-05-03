from django.core.exceptions import ImproperlyConfigured


class RealIP(object):
    def process_request(self, request):
        try:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
        except KeyError:
            raise ImproperlyConfigured("RealIP middleware is active but X-Forwarded-For isn't set.")
