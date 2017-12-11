from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DashboardRedirectView.as_view()),
    # Example: /2012/week/23/
    # url(r'^coach/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.CoachDashboardWeekArchiveView.as_view(),
    #     name="coach-week"),
    # url(r'^player/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.PlayerDashboardWeekArchiveView.as_view(),
    #     name="player-week"),

    url(r'^coach/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.CoachDashboardWeekArchiveView.as_view(),
        name="week"),
    url(r'^player/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.PlayerDashboardWeekArchiveView.as_view(),
        name="week"),
]