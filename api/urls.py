from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^relations/$',views.relationships, name='relationships'),
    url(r'^owners/(.+)/(.+)/$',views.sharers_with_service, name='sharers_with_service'),
    url(r'^owners/(.+)/$',views.sharers, name='sharers'),
    url(r'^moochers/(.+)/(.+)/$',views.moochers_with_service, name='moochers_with_service'),
    url(r'^moochers/(.+)/$',views.moochers, name='moochers'),
    url(r'^users/$', views.add_user, name='add_user'),
    url(r'^users/login/$', views.login_user, name='login_user'),
    url(r'^users/logout/$', views.logout_user, name='logout_user'),
    url(r'^users/logged_in/$', views.logged_in, name='logout_user'),
    url(r'^users/current/$', views.current_user, name='current_user'),
    url(r'^docs/$', views.docs, name='docs'),
    url(r'^cookie/(.+)/(.+)/$', views.transfer_cookie, name='transfer_cookie'),
]
