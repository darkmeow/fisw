from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'inventoryWCG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','django.contrib.auth.views.login',
        {'template_name':'index.html'},name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^lista_items/$','inventory.views.lista_items', name='lista_items'),
    url(r'^item/$','inventory.views.item'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^images/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
),
)
