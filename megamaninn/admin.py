from django.contrib import admin
from megamaninn.models import Customer
from megamaninn.models import Room
from megamaninn.models import Type
from megamaninn.models import Images

# Register your models here.

admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Type)
admin.site.register(Images)