from channels.routing import ProtocolTypeRouter
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
import channels_example.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    # 【channels】添加路由配置指向应用的路由模块
    'websocket': SessionMiddlewareStack(  # 使用Session中间件，可以请求中session的值
        URLRouter(
    		channels_example.routing.websocket_urlpatterns
        )
    ),
})

