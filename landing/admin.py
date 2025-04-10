from django.contrib import admin

from landing.models import BaseModel


# Register your models here.
class LandingAdmin(admin.ModelAdmin):
    list_display =('id', 'name','email', 'message', 'created_at')
    list_display_links = ['id', 'email', 'name']


admin.site.register(BaseModel, LandingAdmin)