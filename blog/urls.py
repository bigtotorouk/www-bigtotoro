from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$',views.list, name="blog_home"),
    url(r'^id/(.+)/$',views.entry, name="blog_entry"),
    url(r'^category/(.+)/$',views.list_category, name="blog_category"),
    # url(r'^comment/(.+)/$',views.comment_insert, name="comment_insert"),
    url(r'^comment/(.+)/$',views.ajax_comment_insert, name="ajax_comment_insert"),
)
