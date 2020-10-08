from django.contrib import admin
from memberapp.models import Member, Association


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'email', 'phone', 'date_of_birth',
        'date_joined', 'active', 'grade')
    list_filter = ('active', 'grade', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

    def render_change_form(
            self, request, context, add=False, change=False,
            form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False,
        })
        return super().render_change_form(
            request, context, add, change, form_url, obj)


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'number_rna', 'number_siren')
    search_fields = ('name', 'email', 'phone', 'number_rna', 'number_siren')

    def render_change_form(
            self, request, context, add=False, change=False,
            form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False,
        })
        return super().render_change_form(
            request, context, add, change, form_url, obj)
