from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^relations$',views.relationships, name='relationships'),
    url(r'^owners/(.+)/$',views.sharers, name='sharers'),
    url(r'^users/', views.add_user, name='add_user'),
]
