from django.conf.urls import url
from django.conf import settings
from django.conf.url.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
   url(r'^sites/(\d+)$', views.project, name='project'),
    url(r'^upload/$', views.upload_site, name='upload'),
    url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
    url(r'^update_profile/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^search/$', views.search, name='search_results'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view())
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)