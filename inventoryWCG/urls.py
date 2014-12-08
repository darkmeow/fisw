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
    url(r'^list_items/$','inventory.views.list_items', name='items_list'),
    url(r'^item/(?P<id_item>[0-9]+)/$','inventory.views.item', name='item_details'),
     url(r'^list_loans/$','inventory.views.list_loans', name='loans_list'),
    url(r'^loan/(?P<id_loan>[0-9]+)/$','inventory.views.loan', name='loan_details'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^images/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}),
    url(r'^wcg_login/$', 'inventory.views.wcg_login'),
    url(r'^dashboard', 'inventory.views.dashboard'),
    url(r'^$', 'inventory.views.index'),
    url(r'^register_item/$', 'inventory.views.register_item'),
    url(r'^register_loan/$', 'inventory.views.register_loan'),
    url(r'^return_loan/(?P<id_loan>[0-9]+)/$', 'inventory.views.return_loan'),
    url(r'^loan_cancel_list/$', 'inventory.views.loan_cancel_list'),
    url(r'^loan_cancel_list_ajax', 'inventory.views.loan_cancel_list_ajax'),
)
