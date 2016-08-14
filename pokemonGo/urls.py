from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pokemon$', 'search.views.index', name = 'index'),
    url(r'^random$', 'search.views.random', name = 'random'),
    url(r'^search$', 'search.views.srch', name = 'search'),
    #un-named grouping
    #url(r'^search/(\d+)', 'search.views.srch2', name = 'search2'),
    #named-grouping
    url(r'^search/(?P<foo>\d+)', 'search.views.srch2', name = 'search2'),
    #url(r'^search/(?P<article_id>[\w\-]+)/$', 'search.views.random', name = 'random'),
)
