"""Chief users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import access,voter_check,stats

router_stats = DefaultRouter()
router_stats.register(r'stats', stats.StatsViewSet, basename='stats')

router_access = DefaultRouter()
router_access.register(r'access', access.AccessViewSet, basename='access')

router_voter_check = DefaultRouter()
router_voter_check.register(
    r'voter/(?P<cid>[-a-zA-Z0-9_]+)/poll',
    voter_check.VoterCheckViewSet,
    basename='voter_polls')

urlpatterns = [
    path('', include(router_voter_check.urls)),
    path('', include(router_access.urls)),
    path('', include(router_stats.urls)),
]
