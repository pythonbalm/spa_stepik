from django.contrib import admin
from .models import Style, House, Features, Photo

class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')
    list_display_links = ('id', 'name', 'text')
    search_fields = ('name',)

# class FeaturesAdmin(admin.ModelAdmin):


admin.site.register(Style, StyleAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Features)
admin.site.register(Photo)