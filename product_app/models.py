from django.urls import reverse
# from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import FloatField
from django.db.models import IntegerField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
# from django_extensions.db import fields as extension_fields


class performance(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True, editable=False)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField(max_length=30)
    revenue = models.FloatField()
    

    # Relationship Fields
    os = models.ForeignKey(
        'product_app.os',
        on_delete=models.CASCADE, related_name="performances", 
    )
    country = models.ForeignKey(
        'product_app.country',
        on_delete=models.CASCADE, related_name="performances", 
    )
    channel = models.ForeignKey(
        'product_app.channel',
        on_delete=models.CASCADE, related_name="performances", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('product_app_performance_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('product_app_performance_update', args=(self.pk,))


class channel(models.Model):

    # Fields
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('product_app_channel_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('product_app_channel_update', args=(self.pk,))


class country(models.Model):

    # Fields
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('product_app_country_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('product_app_country_update', args=(self.pk,))


class os(models.Model):

    # Fields
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('product_app_os_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('product_app_os_update', args=(self.pk,))