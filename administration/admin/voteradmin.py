from django.contrib import admin
from administration.models import Voter

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    """Module where admin can create Polls"""
    list_display = ('cid','name','alive',)
    list_display_links = ('cid',)
    search_fields = ('cid','name')
    readonly_fields = ('registered_date',)
    fieldsets=(
        ('Basics',{'fields': (('cid','name',),('address',),('born_date','alive',),),}),
		('Metadata',{'fields': (('registered_date'),),}),
        )

    def has_delete_permission(self, request, obj=None):
        """Cannot delete."""
        return False
