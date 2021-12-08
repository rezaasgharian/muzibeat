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
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'muzibeat.settings')
django.setup()
# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # We will add WebSocket protocol later, but for now it's just HTTP.
})
