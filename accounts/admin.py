from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import customUserChangeForm,CustomUserCreationForm
from .models import CustomUser
# Register your models here.


class CustomUesrAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = customUserChangeForm
    model = CustomUser
    list_display = ['username','age','email','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('age',)}),
    )
admin.site.register(CustomUser,CustomUesrAdmin)



