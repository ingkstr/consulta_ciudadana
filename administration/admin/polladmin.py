from django.contrib import admin
from administration.models import Poll

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Module where admin can create Polls"""
    list_display = ('pk','name','start_datetime','end_datetime','ready')
    list_display_links = ('pk',)
    search_fields = ('name','slug')
    list_filter = ('start_datetime','end_datetime','ready')
    readonly_fields = ('creation_date','modificated_date','ready',)
    fieldsets=(
        ('Basics',{'fields': (('name',),('slug')),}),
        ('Periodicity',{'fields': (('start_datetime','end_datetime'),),}),
        ('Questions',{'fields': (('question0',),
                                 ('question1',),
                                 ('question2',),
                                 ('question3',),
                                 ('question4',),
                                 ('question5',),
                                 ('question6',),
                                 ('question7',),
                                 ('question8',),
                                 ('question9',),),}),
		('Metadata',{'fields': (('ready'),('creation_date','modificated_date',),),}),
        )

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.ready:
            return self.readonly_fields + ('name','slug','start_datetime','end_datetime','question0','question1','question2','question3','question4','question5','question6','question7','question8','question9')
        return self.readonly_fields

    actions = ['make_ready',]


    def has_delete_permission(self, request, obj=None):
        """Cannot delete."""
        return False

    def make_ready(self, request, queryset):
        """Set poll as ready state. Not modificable"""
        queryset.update(ready=True)
    make_ready.short_description = "Set poll as ready"
