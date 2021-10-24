import os

import django
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from scheduling import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'selfHelp.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    ## IMPORTANT::Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
