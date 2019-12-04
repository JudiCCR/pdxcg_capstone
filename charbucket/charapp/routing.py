from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/charapp/table/(?P<post_id>\d+)/$', consumers.CommConsumer),
    re_path(r'ws/charapp/quickroom/(?P<room_key>\d+)/$', consumers.QuickConsumer),
]