from django.contrib import admin

from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
# schema_view = get_schema_view(
#     openapi.Info(
#         title="BitBuilders API",
#         default_version='v1',
#         description="API documentation for the BitBuilders project",
#         terms_of_service="https://example.com/terms/",
#         contact=openapi.Contact(email="contact@bitbuilders.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="bitbuilders API",
        default_version='v1',
        description="API documentation for the bitbuilders project",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@bitbuilders.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('bitbuilders/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('bitbuilders/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path('api/', include('user.urls')),
    # path('api/', include("order.urls")),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
