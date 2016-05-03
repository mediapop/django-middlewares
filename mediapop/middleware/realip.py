
class RealIP(object):
    def process_request(self, request):
        request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
