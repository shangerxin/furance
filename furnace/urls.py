"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path

from furnace.views.site_map_view import site_map, to_fixture, to_fixture_folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site_map),
    path('fixtures', site_map),
    re_path(r'fixtures/(.*)/(.*\.html)', to_fixture),
    re_path(r'fixtures/(.*)/[^/\.]', to_fixture_folder),
]


