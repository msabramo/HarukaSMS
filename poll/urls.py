from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns(
    '',
    url(r'^dashboard/$', views.dashboard),
    url(r'^latest_messages$',views.latest_messages),
    url(r"^$", views.polls, name="polls"),
    url(r"^(\d+)/submissions.csv$", views.responses_as_csv),
    url(r"^new/$", views.new_poll),
    url(r"^(\d+)/responses/$", views.view_responses, name="poll-responses"),
    url(r"^(?P<poll_id>\d+)/responses/module/$", views.view_responses,  {'as_module':True}, name="poll-responses-module"),
    url(r"^responses/(\d+)/view/$", views.view_response),
    url(r"^(\d+)/report/$", views.view_report, name="poll-report"),
    url(r"^(\d+)/report/(\d+)/$", views.view_report, name="poll-report"),
    url(r"^(?P<poll_id>\d+)/report/module/$", views.view_report, {'as_module':True}, name="poll-report-module"),
    url(r"^(\d+)/report/(\d+)/module/$", views.view_report, {'as_module':True}, name="poll-report-location-module"),

    url(r"^responses/(\d+)/edit/$", views.edit_response),
    url(r"^responses/(\d+)/apply/$", views.apply_response),
    url(r"^responses/(\d+)/apply_all/$", views.apply_all),
    url(r"^responses/(\d+)/delete/$", views.delete_response),
    url(r"^responses/(?P<poll_id>\d+)/stats/$", views.stats, name="poll-stats"),
    url(r"^responses/(?P<poll_id>\d+)/stats/(?P<location_id>\d+)/$", views.stats, name="poll-stats"),
    url(r"^responses/(?P<poll_id>\d+)/numeric/$", views.number_details),
    url(r"^(\d+)/view/$", views.view_poll),
    url(r"^(\d+)/details/$", views.view_poll_details),
    url(r"^(\d+)/edit/$", views.edit_poll),
    url(r"^(\d+)/delete/$", views.delete_poll),
    url(r"^(\d+)/start/$", views.start_poll),
    url(r"^(\d+)/end/$", views.end_poll),
    url(r"^(\d+)/add_category/$", views.add_category),
    url(r"^(\d+)/edit_category/(\d+)/$", views.edit_category),
    url(r"^(\d+)/category/(\d+)/$", views.view_category),
    url(r"^(\d+)/delete_category/(\d+)/$", views.delete_category),
    url(r"^(\d+)/category/(\d+)/rule/(\d+)/$", views.view_rule),
    url(r"^(\d+)/category/(\d+)/rule/(\d+)/edit/$", views.edit_rule),
    url(r"^(\d+)/category/(\d+)/rules/add/$", views.add_rule),
    url(r"^(\d+)/category/(\d+)/rule/(\d+)/delete/$", views.delete_rule),
    url(r"^(\d+)/category/(\d+)/rules/$", views.view_rules),
    url(r"^(\d+)/categories/add/$", views.add_category),
    url(r"^(\d+)/demo/", views.demo, name="demo"),

    url(r"^/activity_as_csv/$", views.activity_as_csv),
)
