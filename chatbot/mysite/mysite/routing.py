from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from jarvis import consumers
websocket_urlPattern=[
    path('ws/jarvis/',consumers.botConsumer.as_asgi()),
]

application=ProtocolTypeRouter({
    # 'http':
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

})