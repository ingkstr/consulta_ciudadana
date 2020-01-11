"""Chief users URLs. """

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import accesspoll


router_consult = DefaultRouter()
router_consult.register(r'consult', accesspoll.PollConsultViewSet, basename='consult')


urlpatterns = [
    path('', include(router_consult.urls)),
]
