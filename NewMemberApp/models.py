# __author__ = 'christopherbelyeu'
# from django.db import models
# from django.utils.translation import ugettext_lazy as _
#
#
# class BaseModel(models.Model):
#     """Abstract base model that all other models should inherit from."""
#     created_at = models.DateTimeField('Created at', auto_now_add=True)
#     modified_at = models.DateTimeField('Modified at', auto_now=True)
#
#     class Meta:
#         abstract = True
#         app_label = "api"
#         verbose_name = _('BaseModel')
#         verbose_name_plural = _('BaseModels')
#
#
# # this is a convenience model to allow Foreign keys to
# #include either kind of address
# class Address(BaseModel):
#     pass
#
#
# class GenericAddress(Address):
#     house_number = models.IntegerField()
#     street = models.CharField(max_length=300)
#     city = models.CharField(max_length=300)
#     state = models.CharField(max_length=300)
#     area_code = models.CharField(max_length=300)
#
#
# class ApartmentAddress(Address):
#     generic_address = models.ForeignKey(GenericAddress)
#     apartment_number = models.CharField(max_length=50)
#
#
# class MembershipEntity(BaseModel):
#     pass
#
#
#
# class Household(MembershipEntity):
#     status = models.CharField(max_length=100)
#     phone = models.CharField(max_length=11)
#     address = models.ForeignKey(Address)
#
#     @staticmethod
#     def get_statuses():
#         return dict('NOT_REQUESTED', 'REQUESTED_NOT_RECEIVED', 'CURRENT_MEMBER', 'MOVE_OUT', 'FORMER')
#
#
# class Member(MembershipEntity):
#     full_name = models.CharField(max_length=300)
#     # household = models.ForeignKey(Household)
#
# class Survey(BaseModel):
#     membership_entity = models.ForeignKey(MembershipEntity)
#
#
# class ChurchUnit(BaseModel):
#     bishop = models.ForeignKey(Member)
#     id = models.IntegerField()
#     # schedule
#
#
# class CustomField(BaseModel):
#     index = models.IntegerField()
#     field_name = models.CharField(max_length=300)
#     unit = models.ForeignKey(ChurchUnit)
#     #this should have a type. date, checkbox, etc...
#
#
# class CustomFieldEntry(BaseModel):
#     field = models.ForeignKey(CustomField)
#     contents = models.CharField(max_length=300)
#     survey = models.ForeignKey(Survey)