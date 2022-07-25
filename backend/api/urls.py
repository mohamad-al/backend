
from django.urls import path , include
from rest_framework import routers
from .views import SearchViewSet , WatchViewSet

router = routers.DefaultRouter()

router.register('search',SearchViewSet)
router.register('watch',WatchViewSet)


urlpatterns = [
    path('',include(router.urls)),

]
 