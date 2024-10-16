from django.contrib import admin
from .models import Currency, Wallet, CurrencyInventory

# Register your models here.
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(CurrencyInventory)