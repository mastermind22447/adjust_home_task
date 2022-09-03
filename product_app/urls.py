from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'performance', api.performanceViewSet)
router.register(r'channel', api.channelViewSet)
router.register(r'country', api.countryViewSet)
router.register(r'os', api.osViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for performance
    path('product_app/performance/', views.performanceListView.as_view(), name='product_app_performance_list'),
    path('product_app/performance/create/', views.performanceCreateView.as_view(), name='product_app_performance_create'),
    path('product_app/performance/detail/<int:pk>/', views.performanceDetailView.as_view(), name='product_app_performance_detail'),
    path('product_app/performance/update/<int:pk>/', views.performanceUpdateView.as_view(), name='product_app_performance_update'),
)

urlpatterns += (
    # urls for channel
    path('product_app/channel/', views.channelListView.as_view(), name='product_app_channel_list'),
    path('product_app/channel/create/', views.channelCreateView.as_view(), name='product_app_channel_create'),
    path('product_app/channel/detail/<int:pk>/', views.channelDetailView.as_view(), name='product_app_channel_detail'),
    path('product_app/channel/update/<int:pk>/', views.channelUpdateView.as_view(), name='product_app_channel_update'),
)

urlpatterns += (
    # urls for country
    path('product_app/country/', views.countryListView.as_view(), name='product_app_country_list'),
    path('product_app/country/create/', views.countryCreateView.as_view(), name='product_app_country_create'),
    path('product_app/country/detail/<int:pk>/', views.countryDetailView.as_view(), name='product_app_country_detail'),
    path('product_app/country/update/<int:pk>/', views.countryUpdateView.as_view(), name='product_app_country_update'),
)

urlpatterns += (
    # urls for os
    path('product_app/os/', views.osListView.as_view(), name='product_app_os_list'),
    path('product_app/os/create/', views.osCreateView.as_view(), name='product_app_os_create'),
    path('product_app/os/detail/<int:pk>/', views.osDetailView.as_view(), name='product_app_os_detail'),
    path('product_app/os/update/<int:pk>/', views.osUpdateView.as_view(), name='product_app_os_update'),
)