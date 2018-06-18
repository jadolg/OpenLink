from django.contrib import admin
from django.contrib.auth.models import Group, User

from LinksList.models import Section, Site


class SitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'url', 'hits')
    readonly_fields = ('active', 'hits')


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Section)
admin.site.register(Site, SitesAdmin)
