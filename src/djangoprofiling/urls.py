import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.conf.urls.static import static

schema_view = get_schema_view(
      openapi.Info(
         title="My Django API",
         default_version='v1',
         description="Test description",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="savva.genchevskiy@gmail.com"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # Pages
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    # API
    path('api/', include('article.urls')),
    path('api/', include('author.urls')),
    path('api/', include('performance.urls')),
    url(r'^silk/', include('silk.urls', namespace='silk')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('sentry-debug/', trigger_error),
    url(r'^health_check/', include('health_check.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
