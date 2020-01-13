from django.urls import path, include
from rest_framework import routers
from .views import MemoViewSet


router = routers.DefaultRouter()
router.register('memos', MemoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
