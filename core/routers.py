from rest_framework_nested import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet,LoginViewSet,RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()


router.register(r'user',UserViewSet,basename="user")

router.register(r'post',PostViewSet,basename="post")

posts_router = routers.NestedSimpleRouter(router,r'post',lookup='post')
posts_router.register(r'comment',CommentViewSet,basename='post-comment')


router.register(r'register',RegisterViewSet,basename="register")
router.register(r'login',LoginViewSet,basename="login")
router.register(r'refresh',RefreshViewSet,basename="refresh")

urlpatterns = [   
    *router.urls,
    *posts_router.urls,
    ]

