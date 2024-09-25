from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('item_list',ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', IndexView.as_view(), name='index'),
    path('items/', ItemView.as_view(), name='item'),
    path('set-cookie/', SetCookieView.as_view(), name='set-cookie'),
    path('get-cookie/', GetCookieView.as_view(), name='get-cookie'),
    path('<str:string>/', IndexView.as_view(), name='index-string'),
]
