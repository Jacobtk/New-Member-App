__author__ = 'christopherbelyeu'
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """Abstract base model that all other models should inherit from."""
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    modified_at = models.DateTimeField('Modified at', auto_now=True)

    class Meta:
        abstract = True
        app_label = "api"
        verbose_name = _('BaseModel')
        verbose_name_plural = _('BaseModels')


class Address(BaseModel):
    house = models.CharField(max_length=300)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    area_code = models.CharField(max_length=300)
    apartment_number = models.CharField(max_length=50, blank=True, null=True)

    def to_string(self):
        return self.house + " " + self.street + ("apt. " + str(
            self.apartment_number) + " ") if self.apartment_number else "" + "\n" + self.city + " " + self.state


class MembershipEntity(BaseModel):
    pass


class Household(MembershipEntity):
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.ForeignKey(Address)

    @staticmethod
    def get_statuses():
        return dict('NOT_REQUESTED', 'REQUESTED_NOT_RECEIVED', 'CURRENT_MEMBER', 'MOVE_OUT', 'FORMER')


class Member(MembershipEntity):
    full_name = models.CharField(max_length=300)
    preferred_name = models.CharField(max_length=300, blank=True, null=True)
    unit = models.ForeignKey('api.ChurchUnit')
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, blank=True, null=True)
    # household = models.ForeignKey(Household)


class Survey(BaseModel):
    membership_entity = models.ForeignKey(MembershipEntity)


class ChurchUnit(BaseModel):
    name = models.CharField(max_length=50)
    bishop = models.ForeignKey(Member)
    id = models.IntegerField(primary_key=True)
    # schedule


class CustomField(BaseModel):
    index = models.IntegerField()
    field_name = models.CharField(max_length=300)
    unit = models.ForeignKey(ChurchUnit)
    # this should have a type. date, checkbox, etc...


class CustomFieldEntry(BaseModel):
    field = models.ForeignKey(CustomField)
    contents = models.CharField(max_length=300)
    survey = models.ForeignKey(Survey)