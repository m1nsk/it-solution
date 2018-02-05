from django.contrib import admin
from .models import Transfer

# Register your models here.


class TransferAdmin(admin.ModelAdmin):
    model = Transfer
    list_display = ('id', 'user_id', 'date', 'type', 'value')


admin.site.register(Transfer, TransferAdmin)
