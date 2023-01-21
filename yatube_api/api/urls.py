from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/follow/', FollowViewSet, name='follow'),
    path('v1/', include('djoser.urls.jwt')),
]
