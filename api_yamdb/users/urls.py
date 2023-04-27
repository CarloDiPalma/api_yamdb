from django.urls import include, path
from rest_framework import routers

from . import views
from .views import UserViewSet

app_name = 'users'

router_v1 = routers.DefaultRouter()
router_v1.register('v1/users', UserViewSet)
router_v1.register('v1/', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', views.signup),
    path('', include(router_v1.urls)),
]
