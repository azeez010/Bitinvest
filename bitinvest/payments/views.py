from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from biti.helpers import enums, utils
from biti import models as biti_models
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings

import datetime
import json
import requests
import uuid
import os


from .models import *
# Create your views here.

def home(request):

    products = Purchase.objects.all()
    return render(request, 'product.html', context = {"products":products})

def exchanged_rate(amount):
    url = "https://www.blockonomics.co/api/price?currency=USD"
    r = requests.get(url)
    response = r.json()
    return amount/response['price']

def track_invoice(request, pk):
    invoice_id = pk
    invoice = Invoice.objects.get(id=invoice_id)
    data = {
            'order_id':invoice.order_id,
            'bits':invoice.btcvalue/1e8,
            'value':invoice.purchase.price,
            'addr': invoice.address,
            'status':Invoice.STATUS_CHOICES[invoice.status+1][1],
            'invoice_status': invoice.status,
            "product_type": invoice.purchase.product_type
        }
    if (invoice.received):
        data['paid'] =  invoice.received/1e8
        if (int(invoice.btcvalue) <= int(invoice.received)):
            data['path'] = invoice.purchase.image_url
    else:
        data['paid'] = 0  
        

    return render(request,'invoice.html',context=data)

@login_required
def create_payment(request, product_type):
    product = None
    purchase = None
    
    if product_type == enums.ProductType.KGS.value:
        kgs_var = request.GET.get('kgs_var')
        price = utils.get_global_variables(kgs_var)
        if "partner_ref_price" == kgs_var:
            type_ = enums.ProductType.PARTNER.value
        elif "trade_ref_price" == kgs_var:
            type_ = enums.ProductType.TRADE.value
        elif "invest_ref_price" == kgs_var:
            type_ = enums.ProductType.INVEST.value
            
        product, _ = biti_models.KGS.objects.get_or_create(product_type=type_, price=price, user=request.user)
        purchase = Purchase.objects.create(product_type=product_type, kgs=product, buyer=request.user, price=price)
    elif product_type == enums.ProductType.TRADE.value:
        trade_id = request.GET.get('id')
        try:
            product = biti_models.Trade.objects.get(id=trade_id)
            price = product.price
            purchase = Purchase.objects.create(product_type=product_type, trade=product, buyer=request.user, price=price)
        except biti_models.Trade.DoesNotExist:
            pass
    elif product_type == enums.ProductType.INVEST.value:
        invest_id = request.GET.get('id')
        try:
            product = biti_models.Invest.objects.get(id=invest_id)
            price = product.price
            purchase = Purchase.objects.create(product_type=product_type, invest=product, buyer=request.user, price=price)
        except biti_models.Invest.DoesNotExist:
            pass
    elif product_type == enums.ProductType.PARTNER.value:
        price = utils.get_global_variables(enums.Settings.PARTNER.value)
        product = biti_models.Partner.objects.create(price=price, user=request.user)
        purchase = Purchase.objects.create(product_type=product_type, partner=product, buyer=request.user, price=price)
    
    # product = Purchase.objects.get(id=product_id)
    url = 'https://www.blockonomics.co/api/new_address'
    headers = {'Authorization': "Bearer " + settings.API_KEY}
    r = requests.post(url, headers=headers)
      
    if product and purchase:   
        if r.status_code == 200:
            address = r.json()['address']
            bits = exchanged_rate(product.price)
            order_id = uuid.uuid1()
            invoice = Invoice.objects.create(order_id=order_id,
                                    address=address,btcvalue=bits*1e8, purchase=purchase)
            return HttpResponseRedirect(reverse('payments:track_payment', kwargs={'pk':invoice.id}))
        else:
            print(r.status_code, r.text)
            return HttpResponse("Some Error, Try Again!")
    else:
        return HttpResponse("Product or purchase not created!")

def receive_payment(request):
    
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    
    invoice.status = int(status)
    
    if (int(status) == 2) and int(value) == invoice.btcvalue :
        if invoice.purchase.product_type == enums.ProductType.KGS.value:
            invoice.purchase.kgs.used = True
        elif invoice.purchase.product_type == enums.ProductType.TRADE.value:
            pass
        elif invoice.purchase.product_type == enums.ProductType.INVEST.value:
            pass
        elif invoice.purchase.product_type == enums.ProductType.PARTNER.value:
            invoice.purchase.buyer.wallet += invoice.purchase.price 
            invoice.purchase.buyer.save()
        
        invoice.purchase.payment_successful = True
        invoice.received = value
        invoice.purchase.save()
        invoice.save()
        
    invoice.txid = txid
    invoice.save()
    return HttpResponse(200)
