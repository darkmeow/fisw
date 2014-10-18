from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'inventoryWCG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','inventory.views.lista_items'),   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    #rl(r'^items/$','inventory.views.items'),
)
