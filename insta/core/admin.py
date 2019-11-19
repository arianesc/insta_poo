'''from django.contrib import admin



admin.site.register(User)'''


from django.contrib import admin
from core.models import User, Foto
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informações pessoais'), {'fields': ('email', 'nome')}),
        (_('Permissões'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Informações pessoais'), {'fields': ('email', 'nome')}),
        (_('Permissões'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Foto)