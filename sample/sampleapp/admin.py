from django.contrib import admin

# Register your models here.
from sampleapp.models import *

admin.site.register(Bio)
admin.site.register(Register)
admin.site.register(CampaignDetail)
admin.site.register(Cars)
admin.site.register(Images)
admin.site.register(Documents)
admin.site.register(CampaignDocuments)
admin.site.register(UserDetail)
