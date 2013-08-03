from djando.conf.urls.defaults import *

urlpatterns = patterns('veggie411.views', 
    url(r'^$', hello, name='hello'),
)
