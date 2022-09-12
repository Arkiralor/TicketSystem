
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import path, include

from core.settings import settings
from core import logger

urlpatterns = [
    path('api/user/', include('user_app.endpoints'))
]

if settings.DEBUG or settings.ENV_TYPE == 'dev':
    urlpatterns += [
        path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('assets/images/favicon.png'))),
        path('admin/', admin.site.urls),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    logger.info('Running in development mode')

## These url patterns are only available in a production environment
elif settings.ENV_TYPE == 'prod' and not settings.DEBUG:
    urlpatterns += [
        path('ticket-system-admin/', admin.site.urls),
    ]

    logger.info('Running in production mode')
