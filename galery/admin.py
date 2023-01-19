from django.contrib import admin
from galery.models import Fotografia



class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("published",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)   