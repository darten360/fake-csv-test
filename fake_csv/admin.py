from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fake_csv.models import User, Schema


@admin.register(User)
class CookAdmin(UserAdmin):
    pass


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass
