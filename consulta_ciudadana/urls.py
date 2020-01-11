"""consulta_ciudadana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.u rls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Public consultation API')

"""
schema_view = get_swagger_view(
   openapi.Info(
      title="Public consultation",
      default_version='v1',
      description="Api to obtain citizen consultation on matters of public impact",
      contact=openapi.Contact(email="ingkstr@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('access.urls', 'access'), namespace='access')),
    path('', include(('publicpoll.urls', 'publicpoll'), namespace='publicpoll')),
    path(r'docs/', schema_view),
]
