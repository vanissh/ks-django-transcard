from django.contrib import admin
from .models import Card, Loadout

class CardAdmin(admin.ModelAdmin):
    list_display = ("inn", "type", "reason", "name", "surname", 'pub_date')
    search_fields = ("inn", )
    list_filter = ("inn", )
    empty_value_display = "-пусто-"
    
class LoadoutAdmin(admin.ModelAdmin):
    list_display = ("st_xls", "sch_xls", "st_images", "sch_images")
    search_fields = ("pub_date", )
    list_filter = ("pub_date", )
    empty_value_display = "-пусто-"

admin.site.register(Card, CardAdmin)
admin.site.register(Loadout, LoadoutAdmin)
