from django.conf.urls import patterns, include, url

from company import views

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$',views.home, name="company_home"),
    url(r'^contact/$',views.contact, name="company_contact"),
    url(r'^portfolio/$',views.portfolio, name="company_portfolio"),
)
