from rest_framework.throttling import SlidingRateThrottle


class DictionaryAnonSlidingThrottle(SlidingRateThrottle):
    scope = 'dictionary_anon'


class DictionaryUserSlidingThrottle(SlidingRateThrottle):
    scope = 'dictionary_user'
