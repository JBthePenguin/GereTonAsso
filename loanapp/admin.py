from django.contrib import admin
from loanapp.models import LoanMadeToMemberMaterial


@admin.register(LoanMadeToMemberMaterial)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in LoanMadeToMemberMaterial._meta.get_fields()]
    # list_display = (
    #     'last_name', 'first_name', 'email', 'phone', 'date_of_birth',
    #     'date_joined', 'active', 'grade')
    # list_filter = ('active', 'grade')
    # search_fields = ('first_name', 'last_name', 'email',)
