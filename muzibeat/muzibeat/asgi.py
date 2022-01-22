"""
ASGI config for muzibeat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
from django.core.handlers.asgi import ASGIHandler

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# from muzibeat.chat import routing
# import muzibeat.chat.routing
# from muzibeat.chat.routing import *
# import chat.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muzibeat.settings')
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# application = AsgiHandler()
application = ProtocolTypeRouter({
    "http": ASGIHandler(),
    # "websocket": AuthMiddlewareStack(
    #     URLRouter(
    #         chat.routing.websocket_urlpatterns
    #     )
    # ),
    # We will add WebSocket protocol later, but for now it's just HTTP.
})

# "http": get_asgi_application(),
# "websocket": AuthMiddlewareStack(
#     URLRouter(
#         chat.routing.websocket_urlpatterns
#     )
# ),
