from django.contrib import admin
from .models import Lead

# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('fullname', 'email', 'phone', 'plan', 'created_at')


admin.site.register(Lead, LeadAdmin)