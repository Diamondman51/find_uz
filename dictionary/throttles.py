from rest_framework.throttling import ScopedRateThrottle

class DictionaryAnonSlidingThrottle(ScopedRateThrottle):
    scope = 'dictionary_anon'


class DictionaryUserSlidingThrottle(ScopedRateThrottle):
    scope = 'dictionary_user'
