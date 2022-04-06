"""EZLifeProject URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

router = DefaultRouter()

schema_view = get_schema_view(title='Bookings API', description='An API to book matches or update odds.')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),

    path('ApartmentOwnerApp/', include('ApartmentOwnerApp.urls')),
    path('ApartmentNumberApp/', include('ApartmentNumberApp.urls')),
    path('ParkingNumberApp/', include('ParkingNumberApp.urls')),
    path('CarNumberApp/', include('CarNumberApp.urls')),
    path('MotorcycleNumberApp/', include('MotorcycleNumberApp.urls')),
    path('TreeApp/', include('TreeApp.urls')),

    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Bookings API')),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^Django_Upload_Files/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
