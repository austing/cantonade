from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from librairie.views import TagTexteList, AuteurTexteList, TexteDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    (r'^tag/([\w-]+)/$', TagTexteList.as_view()),
    (r'^auteur/([\w-]+)/$', AuteurTexteList.as_view()),
    (r'^texte/([\w-]+)/$', TexteDetailView.as_view()),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^colophon/$', 'flatpage', {'url': '/colophon/'}, name='colophon'),
    url(r'^/$', 'flatpage', {'url': '/'}, name='index'),
)