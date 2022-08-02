from django.db import router
from rest_framework import routers
from .api import LeedViewset


router = routers.DefaultRouter()

router.register('api/leeds', LeedViewset, 'leeds')
urlpatterns = router.urls