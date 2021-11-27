from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="TulaHack API",
        default_version='v1',
        description="""API for mobile application""",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path('', include('account.urls')),
    path('', include('finance.urls')),
    path('', include('fitness.urls')),
]

urlpatterns += i18n_patterns(

    path('api/', include((api_patterns, 'API'), namespace='api')),

    prefix_default_language=settings.I18N_PREFIX_DEFAULT_LANGUAGE
)

urlpatterns += [
        path('api/', RedirectView.as_view(url='/swagger/', permanent=True)),
        path('', RedirectView.as_view(url='/docs/', permanent=True)),
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
