from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bases.views.home', name='home'),
    # url(r'^bases/', include('bases.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('bases_core.views',
    url(r'^$', 'index'),
    url(r'^about/$', 'about'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^comments/', include('django.contrib.comments.urls')),
)

# ebootcamp
urlpatterns += patterns('',
    url(r'^ebootcamp/', include('ebootcamp.urls')),
)    
