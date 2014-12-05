from rest_framework import viewsets
from models import Member, Household, Survey, ChurchUnit, Address
from django.views.generic.base import TemplateView
from serializers import MemberSerializer, HouseholdSerializer, SurveySerializer, ChurchUnitSerializer, AddressSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class ChurchUnitViewSet(viewsets.ModelViewSet):
    queryset = ChurchUnit.objects.all()
    serializer_class = ChurchUnitSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer