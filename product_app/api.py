from . import models
from . import serializers
from rest_framework import viewsets, permissions


class performanceViewSet(viewsets.ModelViewSet):
    """ViewSet for the performance class"""

    queryset = models.performance.objects.all()
    serializer_class = serializers.performanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class channelViewSet(viewsets.ModelViewSet):
    """ViewSet for the channel class"""

    queryset = models.channel.objects.all()
    serializer_class = serializers.channelSerializer
    permission_classes = [permissions.IsAuthenticated]


class countryViewSet(viewsets.ModelViewSet):
    """ViewSet for the country class"""

    queryset = models.country.objects.all()
    serializer_class = serializers.countrySerializer
    permission_classes = [permissions.IsAuthenticated]


class osViewSet(viewsets.ModelViewSet):
    """ViewSet for the os class"""

    queryset = models.os.objects.all()
    serializer_class = serializers.osSerializer
    permission_classes = [permissions.IsAuthenticated]
