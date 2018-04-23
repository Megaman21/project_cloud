from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from megamaninn.models import Customer, profile
from megamaninn.models import Room
from megamaninn.models import Type
from megamaninn.models import Images

# Register your models here.

class ProfileInLine(admin.StackedInline):
    model=profile
    can_delete=False
    verbose_name_plural = 'Profile'
    fk_name='user'

class CustomUserAdmin(UserAdmin):
    inlines=(ProfileInLine,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()

        return super(CustomUserAdmin, self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Type)
admin.site.register(Images)