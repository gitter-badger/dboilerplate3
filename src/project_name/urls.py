from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

####################################################
# Default URL patterns, you shouldn't modify this  #
####################################################

sitemaps = {
    # Put here your functions from apps.appsitemap
    #'flatpages': FlatPageSitemap,
    #'blog': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('',

    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

####################################################
# Your app URL patterns                            #
####################################################

urlpatterns += patterns('',
    #url(r'^$', include('apps.{{my_app}}.urls')) ## Example
)
