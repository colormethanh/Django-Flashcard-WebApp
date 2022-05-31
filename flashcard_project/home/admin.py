from django.contrib import admin
from .models import Set, Card

# Register your models here.


class SetAdmin(admin.ModelAdmin):
   prepopulated_fields = {"slug": ("name",)}

admin.site.register(Set, SetAdmin)
admin.site.register(Card)