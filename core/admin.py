from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Account, Table


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'capacity', 'is_busy', 'short_description')


admin.site.register(Account, AccountAdmin)
admin.site.register(Table, TableAdmin)
