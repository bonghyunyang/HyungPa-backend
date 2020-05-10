import json
from .models import Review,ReviewComment
from django.views import View
from django.http import JsonResponse

class ReviewDetailView(View):
    def get(self, request, review_id):
        if Review.objects.filter(id=review_id).exists():
            review = Review.objects.get(id=review_id)
            content = {
                'description' : review.description,
                'likenumber'  : review.like_number,
                'feedtime'    : review.published_at,
                'viewnumber'  : review.view_number,
            }
            return JsonResponse({'content': content}, status = 200)

        return JsonResponse({'message': 'REVIEW_DOES_NOT_EXIST'}, status = 404)

class ReviewCommentView(View):

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
            review_elements = Review.objects.all().values('id','like_number','published_at','view_number','first_image','first_comment')[offset : offset + limit]
            return JsonResponse({'review_main': list(review_elements)}, status = 200)

        except Review.DoesNotExist:
            return JsonResponse({'message':'review_does_not_exist'}, status = 404)

class ReviewReplyView(View):
    def get(self, request):
        return JsonResponse({'comment':[]}, status=200)