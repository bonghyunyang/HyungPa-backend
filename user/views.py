from product.models   import *
from post.models      import *
from django.db.models import Avg
import random

from django.views     import View
from django.http      import JsonResponse

class HomeView(View):
    def get(self, request):
        category         = random.randrange(1, len(SecondCategory.objects.all()))
        product_category = SecondCategory.objects.prefetch_related('product_set').get(id = category)
        products         = product_category.product_set.all().order_by('-like_nums')

        product_ranking      = [
            {'id'           : product.id,
             'category'     : product_category.name,
             'brand'        : product.brand_name,
             'productName'  : product.name,
             'productImage' : product.product_image,
             'rate'         : [UserScore.objects.filter(product_id = product.id).aggregate(Avg('score'))['score__avg'],
                               len(UserScore.objects.filter(product_id = product.id))]
             } for product in products[:4]]

        brand_rand   = random.randrange(1, len(Product.objects.all()))
        brand_get    = Product.objects.get(id = brand_rand)
        brands       = Product.objects.filter(brand_name = brand_get.brand_name).order_by('-like_nums')
        brand_ranking = [
            {'id'           : brand.id,
             'brand'        : brand.brand_name,
             'productName'  : brand.name,
             'productImage' : brand.product_image,
             'rate'         : [UserScore.objects.filter(product_id = brand.id).aggregate(Avg('score'))['score__avg'],
                               len(UserScore.objects.filter(product_id = brand.id))]
        } for brand in brands[:4]]

        power_reviews = Post.objects.order_by('?')[:7]
        review = [
            {'id': power_review.id,
             'title': power_review.title,
             'likes': power_review.like_number,
             'views': power_review.view_number
             } for power_review in power_reviews]


        return JsonResponse({'ProductData1' : product_ranking, 'BrandData2' : brand_ranking, 'PostData3' : review}, status = 200)