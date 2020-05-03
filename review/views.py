import json
import datetime
from utils import user_authentication
from .models import Review,ReviewComment
from user.models import User
from product.models import Product
from django.views import View
from django.http import HttpResponse, JsonResponse

class ReviewDetailView(View):
    
    def get(self, request,review_id):
        if Review.objects.filter(id = review_id).exists():
            review = Review.objects.get(id=review_id)
            
            review_attribute = {
                'description' : review.description,
                'like' : review.like_number,
                'view' : review.view_number,
                'postDate' : datetime.datetime.strftime(review.published_at, '%Y.%m.%d'),
            }
            return JsonResponse({'review': review_attribute}, status = 200)
        
        return JsonResponse({'message': 'REVIEW_DOES_NOT_EXIST'}, status = 404)
    
class ReviewCommentView(View):
    
    @user_authentication
    def post(self, request):
        data = json.loads(request.body)
        if 'is_original' in data:
            ReviewComment(
                comment     = data['comment'],
                review_id   = data['review_id'],
                user_id     = data['user_id'],
                is_original = True,
            ).save()
        else:
            ReviewComment(
                comment     = data['comment'],
                review_id   = data['review_id'],
                user_id     = data['user_id'],
                is_original = False,
                original_comment_id = data['original_comment'],
            ).save()
        return JsonResponse({'message': 'SUCCESS'}, status = 200)

class ReviewView(View):
 
    def get(self, request):
        offset = int(request.GET.get('offset'))
        limit  = int(request.GET.get('limit'))
        
        
        try:
                        
            review_elements = Review.objects.all() #[offset : offset + limit-1]
            user = User.objects.all()

            
            review_attribute = [{
                'description' : review.description,
                'like'    : review.like_number,
                'view'    : review.view_number,
                'postdate': review.published_at,
                'product_img' : review.product.product_image,
                'brand'   : review.product.brand_name,
                'product' : review.product.name,
            }for review in review_elements[offset : offset + limit-1]]
            
            return JsonResponse({'review_main': review_attribute}, status = 200)
        
        except Review.DoesNotExist:
            return JsonResponse({'message': 'REVIEW_DOES_NOT_EXIST'}, status = 404)

        