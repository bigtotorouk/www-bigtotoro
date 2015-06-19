from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'company.views.home', name='company_home'),
    url(r'^profile/portfolio/$','company.views.portfolio', name="company_portfolio"),
    url(r'^blog/', include('blog.urls')),
    url(r'^company/', include('company.urls')),
    url(r'^/wherecoffee/order$', 'wherecoffee.views.order', name='wherecoffee_order'),

    #url(r'^news/', include('news.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
   urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
        url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), )