from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'inventoryWCG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$','django.contrib.auth.views.login',
    #    {'template_name':'index.html'},name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^lista_items/$','inventory.views.lista_items', name='lista_items'),
    url(r'^item/(?P<id_item>[0-9])/$','inventory.views.item', name='detalle_item'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^images/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}),
    url(r'^wcg_login/$', 'inventory.views.wcg_login'),
    url(r'^dashboard', 'inventory.views.dashboard'),
    url(r'^$', 'inventory.views.index'),

    
    url(r'^test_form/', 'inventory.views.test_form'),
)
