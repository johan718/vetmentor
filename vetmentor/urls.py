import os.path
from django.conf.urls import patterns, include
from mentor.views import contact, LandingView, SignupView, thanks
from django.contrib import admin

admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__),'site_media'
)

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)$',
     'django.views.static.serve',{'document_root':site_media}),
    (r'^$', LandingView.as_view()),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', thanks),
    (r'^signup$', SignupView.as_view()),
    #(r'^accounts/', include('allauth.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$',
    'django.views.static.serve',{'document_root':site_media}),
)
