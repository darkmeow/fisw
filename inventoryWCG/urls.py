from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'inventoryWCG.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$','django.contrib.auth.views.login',
    #    {'template_name':'index.html'},name='login'),
    #url(r'^images/(?P<path>.*)$',   'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^logout/$',               'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^admin/',                 include(admin.site.urls)),
    url(r'^admin/doc/',             include('django.contrib.admindocs.urls')),
    url(r'^',                       include('inventory.urls'))
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
