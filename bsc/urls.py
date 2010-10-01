import os

from django.conf import settings
from django.conf.urls.defaults import *
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^json/news/get$', 'bsc.news.views.get_news'),
    (r'^$', 'bsc.homepage.views.index'),

    (r'^', include('bsc.announcement.urls')),
    (r'^', include('bsc.planetarium.urls')),

    # Example:
    # (r'^bsc/', include('bsc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^m/(?P<path>.*)$', serve, {
            'document_root' : os.path.join(os.path.dirname(__file__), 'media')
        })
    )
