from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from ICA.views import home, success, profile
from registration_stud.views import register_stud
from registration_prof.views import register_prof

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',home),
    url(r'^registration_stud/$',register_stud),
    url(r'^registration_prof/$',register_prof),
    url(r'^success/$',success),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', profile),
)
