from product.models   import *
from post.models      import *
from django.db.models import Avg
import random

from django.views     import View
from django.http      import JsonResponse

class ProductRankingView(View):
    def get(self, request):
        category = random.randrange(1, SecondCategory.objects.count())
        products = Product.objects.filter(secondcategory_id=category).order_by('-like_nums')

        product_ranking = [
            {'id': product.id,
             'category': product.secondcategory.name,
             'brand': product.brand_name,
             'productName': product.name,
             'productImage': product.product_image,
             'rate': [UserScore.objects.filter(product_id=product.id).aggregate(Avg('score'))['score__avg'],
                      len(UserScore.objects.filter(product_id=product.id))]
             } for product in products[:4]]

        return JsonResponse({'ProductData1' : product_ranking}, status = 200)

class BrandRankingView(View):
    def get(self, request):
        brand_rand   = random.randrange(1, Product.objects.count())
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

        return JsonResponse({'BrandData2' : brand_ranking}, status = 200)

class NewpickView(View):
    def get(self, request):
        new_picks = Product.objects.order_by('?')[:7]
        new_pick = [
            {'id': new_pick.id,
             'brand': new_pick.brand_name,
             'productName': new_pick.name,
             'productImage': new_pick.product_image
             } for new_pick in new_picks]

        return JsonResponse({'PickData3': new_pick}, status=200)

class ProductView(View):
    def get(self, request):
        firstcategory   = request.GET.get('category', None)
        offset          = int(request.GET.get('offset'))
        limit           = int(request.GET.get('limit'))

        category_dict   = {}
        if firstcategory:
            category_dict['firstcategory'] = firstcategory
        products = Product.objects.filter(**category_dict).order_by('-like_nums')
        product_ranking      = [
            {'id'           : product.id,
             'brand'        : product.brand_name,
             'productName'  : product.name,
             'productImage' : product.product_image,
             'rate'         : [UserScore.objects.filter(product_id = product.id).aggregate(Avg('score'))['score__avg'],
                               len(UserScore.objects.filter(product_id = product.id))]
             } for product in products[offset : offset + limit]]

        return JsonResponse({'products': product_ranking}, status = 200)

class ProductDetailView(View):
    def get(self, request, product_id):
        product         = Product.objects.get(id = product_id)
        product_scores  = UserScore.objects.filter(product_id = product_id)

        score           = []
        score_dict      = {0.0 : 0, 0.5 : 0, 1.0 : 0, 1.5 : 0, 2.0 : 0, 2.5 : 0, 3.0 : 0, 3.5 : 0, 4.0 : 0, 4.5 : 0, 5.0 : 0}

        for product_score in product_scores:
            score.append(product_score.score)

        for key in score_dict:
            score_dict[key] = score.count(key)

        product_details = [
            {'brand'            : product.brand_name,
             'productName'      : product.name,
             'productImage'     : product.product_image,
             'likes'            : product.like_nums,
             'powerReview'      : product.review_nums,
             'miniReview'       : product.mini_nums,
             'count'            : product.capacity,
             'price'            : product.price,
             'rateData'         : list(score_dict.values())
             }]

        power_reviews = Post.objects.order_by('?')[:7]
        review = [
            {'id'           : power_review.id,
             'title'        : power_review.title,
             'image'        : power_review.first_image,
             'likes'        : power_review.like_number,
             'views'        : power_review.view_number
             } for power_review in power_reviews]

        return JsonResponse({'product_data': product_details, 'review_data' : review}, status = 200)