import json
import datetime
from .models import Product,UserScore


from django.db.models import Sum, Avg
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.


class ReviewProductView(View):
     
    def get(self, request,product_id):
        if Product.objects.filter(id = product_id).exists():
            product = Product.objects.get(id=product_id)
            
            product_attribute = {
                'image' : product.product_image,
                'brand' : product.brand_name,
                'product' : product.name,
                'rate' : UserScore.objects.filter(product_id = product.id).aggregate(Avg('score'))['score__avg'],
                'like' : 'asdf'
            }
            return JsonResponse({'product': product_attribute}, status = 200)
        
        return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIST'}, status = 404)