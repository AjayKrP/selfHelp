from django.conf.urls import url
from scheduling.consumers import SelfHelpConsumer

websocket_urlpatterns = [
    url(r'^ws/go/(?P<room_code>\w+)/$', SelfHelpConsumer.as_asgi()),
]
