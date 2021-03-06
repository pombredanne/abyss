from django.conf.urls import patterns, url

from apps import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ListApp.as_view(), name='list-app'),
    url(r'^create/$', views.CreateApp.as_view(), name='create-app'),
    url(r'^run/$', views.Run.as_view(), name='run'),
    url(r'^(?P<app_name>[\w-]+)/$',
        views.AppDetail.as_view(), name='detail-app'),
    url(r'^(?P<name>[\w-]+)/remove/$',
        views.RemoveApp.as_view(), name='remove_app'),
    url(r'^(?P<app_name>[\w-]+)/log/$', views.AppLog.as_view(),
        name='app_log'),
    url(r'^(?P<app_name>[\w-]+)/env/$', views.AppEnv.as_view(),
        name='get-env'),
    url(r'^(?P<app_name>[\w-]+)/teams/$',
        views.AppTeams.as_view(), name='app-teams'),
    url(r'^(?P<app_name>[\w-]+)/team/add/$',
        views.AppAddTeam.as_view(), name='app-add-team'),
    url(r'^(?P<app_name>[\w-]+)/units/$',
        views.ChangeUnit.as_view(), name='change-units'),
)
