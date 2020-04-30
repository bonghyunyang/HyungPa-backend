from product.models import *
from django.db.models import Sum
import random

from django.views   import View
from django.http    import JsonResponse

class RankingView(View):
    def get(self, request):
        category         = random.randrange(1,102)
        product_category = SecondCategory.objects.prefetch_related('product_set').get(id = category)
        products         = product_category.product_set.all().order_by('-like_nums')

        product_ranking      = [
            {'id'           : product.id,
             'brand'        : product.brand_name,
             'productName'  : product.name,
             'productImage' : product.product_image,
             'rate'         : [UserScore.objects.filter(product_id = product.id).aggregate(Sum('score'))['score__sum']/len(UserScore.objects.filter(product_id = product.id)),
                               len(UserScore.objects.filter(product_id = product.id))]
             } for product in products[:4]]

        brands      = Product.objects.filter(brand_name = "이니스프리").order_by('-like_nums')
        brand_ranking = [
            {'id'           : brand.id,
             'brand'        : brand.brand_name,
             'productName'  : brand.name,
             'productImage' : brand.product_image,
             'rate'         : [UserScore.objects.filter(product_id = brand.id).aggregate(Sum('score'))['score__sum'],
                               len(UserScore.objects.filter(product_id = brand.id))]
        } for brand in brands[:4]]

        new_picks   = Product.objects.order_by('?')[:7]
        new_pick = [
            {'id'           : new_pick.id,
             'brand'        : new_pick.brand_name,
             'productName'  : new_pick.name,
             'productImage' : new_pick.product_image
        } for new_pick in new_picks]

        return JsonResponse({'ProductData1' : product_ranking, 'BrandData2' : brand_ranking, 'PickData3' : new_pick}, status = 200)

class ProductView(View):
    def get(self, request):
        firstcategory   = request.GET.get('category', None)
        products             = Product.objects.filter(firstcategory_id = firstcategory).order_by('-like_nums')
        product_ranking      = [
            {'id'           : product.id,
             'brand'        : product.brand_name,
             'productName'  : product.name,
             'productImage' : product.product_image,
             'rate'         : [UserScore.objects.filter(product_id = product.id).aggregate(Sum('score'))['score__sum']/len(UserScore.objects.filter(product_id = product.id)),
                               len(UserScore.objects.filter(product_id = product.id))]
             } for product in products]

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

        return JsonResponse({'product_data': product_details}, status = 200)