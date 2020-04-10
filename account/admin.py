from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from account.models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "date_created",
        "last_updated",
        "is_admin",
        "is_staff",
    )
    search_fields = ("email", "email")
    readonly_fields = ("date_created", "last_updated")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
