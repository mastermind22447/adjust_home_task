from . import models

from rest_framework import serializers


class performanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.performance
        fields = (
            'pk', 
            'name', 
            'created', 
            'impressions', 
            'clicks', 
            'installs', 
            'spend', 
            'revenue', 
        )


class channelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.channel
        fields = (
            'pk', 
            'name', 
        )


class countrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.country
        fields = (
            'pk', 
            'name', 
        )


class osSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.os
        fields = (
            'pk', 
            'name', 
        )


