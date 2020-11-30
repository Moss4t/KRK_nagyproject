from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog
from machina import urls as machina_urls


js_info_dict = {
    'packages': ('base', ),
}

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript_catalog'),

    # Admin

    path('admin/', admin.site.urls),
    # Apps
    path('', include('KRK_Forum.apps.auth.urls')),
    path('', include(machina_urls)),
]

