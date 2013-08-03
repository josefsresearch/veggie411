from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'veg.views.home', name='home'),
    # url(r'^veg/', include('veg.foo.urls')),
    #mine=url(r'^veggie411/', include('veggie411.urls')),
    url(r'^hello/', 'veggie411.views.hello', name='hello'),
    url(r'^$', 'veggie411.views.home', name='home'),
    url(r'^home/', 'veggie411.views.home', name='home'),
    url(r'^submitemail/', 'veggie411.views.submitemail', name='submitemail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
