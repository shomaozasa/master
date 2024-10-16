from django.db import models

# Create your models here.

#通貨テーブル
class Currency(models.Model):
    denomination = models.IntegerField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#ユーザーの財布テーブル
class Wallet(models.Model):
    user_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#財布内の通貨テーブル
class CurrencyInventory(models.Model):
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE)
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)