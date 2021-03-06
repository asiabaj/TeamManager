from django.conf.urls import url

from . import views


app_name = 'trainings'

urlpatterns = [


    url(r'^/', views.redirect_view, name='redirect-view'),

    url(r'^team/(?P<team_id>\d+)/new/$', views.training_new, name='training-new'),
    url(r'^(?P<event_id>\d+)/$', views.event_detail, name="event-detail"),
    url(r'^team/(?P<team_id>\d+)/training/(?P<event_id>\d+)/delete/$', views.training_delete, name="training-delete"),
    url(r'^(?P<event_id>\d+)/share/$', views.training_share, name="training_share"),


    # /trainings/team/1/year/2017/week/50/
    url(r'^team/(?P<team_id>\d+)/year/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.event_team_week_list,
        name='event-team-week-list'),

    url(r'^year/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.event_user_week_list,
        name='event-user-week-list'),

    url(r'^matches/$', views.matches_list, name='matches_list'),
]
