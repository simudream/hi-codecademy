from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^tile/(?P<coords>.*)$', 'src.views.tileimg'),
    url(r'^add-marker/', 'src.views.addmarker'),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT}),
    url(r'$', 'src.views.index'),
)
