
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from api.viewsets import CarViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register("api/cars",CarViewSet,basename='car_api')

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/schema/ui/', SpectacularSwaggerView.as_view()),
] + router.urls
