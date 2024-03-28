# coding=utf-8
"""Dinopedia api v1 urls."""
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.apis.v1.views import UserRegisterViewSetV1
from dinosaurs.apis.v1.views import DinosaurViewSetV1, UserFavoriteDinosaursViewSetV1

router = SimpleRouter()
router.register(r'api/v1/dinosaurs', DinosaurViewSetV1)
router.register(r'api/v1/user-favorite-dinosaurs', UserFavoriteDinosaursViewSetV1, basename='user-favorite-dinosaurs')

urlpatterns = router.urls + [
    path(r'api/v1/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path(r'api/v1/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path(r'api/v1/register/', UserRegisterViewSetV1.as_view({'post': 'create'}), name='user-register'),
]

app_name = 'api_v1'
