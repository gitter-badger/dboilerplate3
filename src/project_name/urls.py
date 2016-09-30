from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

admin.autodiscover()

####################################################
# Default URL patterns, you shouldn't modify this  #
####################################################

sitemaps = {
    # Put here your functions from apps.appsitemap
    # 'flatpages': FlatPageSitemap,
    # 'blog': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = [
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps})
]

####################################################
# Your app URL patterns                            #
####################################################

urlpatterns += [
    # url(r'^$', include('apps.{{my_app}}.urls')) ## Example
]
