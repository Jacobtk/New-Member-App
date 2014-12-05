from rest_framework import serializers
from models import Member
from models import Household
from models import Survey
from models import ChurchUnit


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


