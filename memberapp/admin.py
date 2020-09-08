from django.contrib import admin
from django.utils.html import format_html
from memberapp.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'email', 'phone', 'date_of_birth',
        'date_joined', 'active', 'grade')
    list_filter = ('active', 'grade')
    search_fields = ('first_name', 'last_name', 'email',)
