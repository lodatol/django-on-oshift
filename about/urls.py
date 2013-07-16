from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns(
    'about',
    url(r'^$', AboutView.as_view(), name='about'),
)


from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)