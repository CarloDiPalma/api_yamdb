from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
#
# router = routers.DefaultRouter()
# router.register('posts', PostViewSet)
# router.register('groups', GroupViewSet)
# router.register('follow', FollowViewSet, basename='follow')
# router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    # path('v1/', include(router.urls)),
    # path('v1/', include('djoser.urls.jwt')),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
