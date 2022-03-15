from django.urls import path, include
from apitest.views import ProductViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'prodotti', ProductViewSet)

app_name = 'apitest'

urlpatterns = [
    path('',include(router.urls)),
]