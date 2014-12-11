from rest_framework import serializers
from models import Member
from models import Household
from models import Survey
from models import ChurchUnit
from models import Address
from django.contrib.auth.models import User


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member


class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey


class ChurchUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchUnit


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
