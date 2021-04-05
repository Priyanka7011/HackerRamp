from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import clientRoom.routing
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
	"http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            clientRoom.routing.websocket_urlpatterns
        )
    ),
})
