#!/usr/bin/env python3

from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    # url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.SyncConsumer),
    url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.AsyncConsumer),
]

