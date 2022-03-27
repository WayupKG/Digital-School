from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    path("i18n/", include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include("Core.urls")),    
    path('school/', include("School.urls")),    
    path('accounts/', include("User.urls")),    
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += i18n_patterns(path('__debug__/', include(debug_toolbar.urls)),)