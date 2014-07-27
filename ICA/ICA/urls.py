from django.conf.urls import patterns, include, url
from ICA.views import home
from registration_stud.views import register_stud

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$',home),
    url(r'^registration_stud/$',register_stud),
    url(r'^admin/', include(admin.site.urls)),
)
