from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
import views

# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer
#
#
# class HouseholdViewSet(viewsets.ModelViewSet):
#     queryset = Household.objects.all()
#     serializer_class = HouseholdSerializer
#
#
# class SurveyViewSet(viewsets.ModelViewSet):
#     queryset = Survey.objects.all()
#     serializer_class = SurveySerializer
#
#
# class ChurchUnitViewSet(viewsets.ModelViewSet):
#     queryset = ChurchUnit.objects.all()
#     serializer_class = ChurchUnitSerializer
#


admin.autodiscover()

router = DefaultRouter(trailing_slash=False)
router.register(r'units', views.ChurchUnitViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'households', views.HouseholdViewSet)
router.register(r'surveys', views.SurveyViewSet)
router.register(r'addresses', views.AddressViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^unit/(?P<pk>\d+)/entries/$', views.CustomFieldByUnitViewSet.as_view(),
                           name='Unit-Custom-Field'),
    url(r'^CustomField/(?P<pk>\d+)/Entries/$', views.CustomFieldEntryByCustomField.as_view(),
                           name='Entry-By-Field'),
)