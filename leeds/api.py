from .models import Leed
from rest_framework import viewsets, permissions
from .serializers import LeedSerializer


class LeedViewset(viewsets.ModelViewSet):
    queryset = Leed.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeedSerializer