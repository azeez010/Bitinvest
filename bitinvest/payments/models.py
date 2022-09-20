from django.db import models
from biti import models as biti_models
from biti.helpers import enums

class Purchase(models.Model):
    product_type = models.CharField(max_length=50, choices=enums.ProductType.choices(), null=False, blank=False)
    kgs = models.ForeignKey(biti_models.KGS, on_delete=models.CASCADE,  null=True, blank=True, related_name="product_kgs")
    trade = models.ForeignKey(biti_models.Trade, on_delete=models.CASCADE,  null=True, blank=True, related_name="product_trade")
    invest = models.ForeignKey(biti_models.Invest, on_delete=models.CASCADE,  null=True, blank=True, related_name="product_invest")
    partner = models.ForeignKey(biti_models.Partner, on_delete=models.CASCADE,  null=True, blank=True, related_name="product_partner")
    buyer = models.ForeignKey(biti_models.User, on_delete=models.CASCADE,  null=True, blank=True, related_name="product_buyer")
    image_url = models.URLField(max_length=200, blank=True, null=True)
    price = models.FloatField(default=0.0)
    payment_successful = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product_type

class Invoice(models.Model):
    STATUS_CHOICES = ((-1,"Not Started"),(0,'Unconfirmed'), (1,"Partially Confirmed"), (2,"Confirmed"))

    purchase = models.ForeignKey("Purchase", on_delete=models.CASCADE, related_name="purchase_invoice")
    status = models.IntegerField(choices=STATUS_CHOICES, default=-1)
    order_id = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)
    btcvalue = models.IntegerField(blank=True, null=True)
    received = models.IntegerField(blank=True, null=True)
    txid = models.CharField(max_length=250, blank=True, null=True)
    rbf = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.address
    