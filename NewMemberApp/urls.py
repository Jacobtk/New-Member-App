from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import views


admin.autodiscover()

router = DefaultRouter(trailing_slash=False)

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
