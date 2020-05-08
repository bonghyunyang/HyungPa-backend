import json
import datetime

from .models    import Post, PostComment
from user.models import User

from django.views       import View
from django.http        import HttpResponse, JsonResponse

class PostDetailView(View):
    def get(self, request, post_id):
        if Post.objects.filter(id = post_id).exists():
            post = Post.objects.get(id = post_id)
            post_attribute = {
                              'title'       : post.title,
                              'description' : post.description,
                              'like'        : post.like_number,
                              'view'        : post.view_number,
                              'postDate'    : post.published_at,
	    }
            return JsonResponse({'post': post_attribute}, status = 200)

        return JsonResponse({'message': 'post_does_not_exist'}, status = 404)

class PostCommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        if 'is_original' in data:
            PostComment(
                comment     = data['comment'],
                post_id     = data['post_id'],
                user_id     = data['user_id'],
                is_original = True,
            ).save()
        else:
            PostComment(
                comment     = data['comment'],
                post_id     = data['post_id'],
                user_id     = data['user_id'],
                is_original = False,
                original_comment_id = data['original_comment'],
            ).save()
        return JsonResponse({'message': "success"}, status = 200)

class PostView(View):
    def get(self, request):
        offset = int(request.GET.get('offset'))
        limit  = int(request.GET.get('limit'))
        try:
            post_elements = Post.objects.all().values('id', 'title', 'like_number','published_at','view_number','first_image', 'first_text')[offset : offset + limit]
            return JsonResponse({'post_main': list(post_elements)}, status = 200)

        except Post.DoesNotExist:
            return JsonResponse({'message':'post_does_not_exist'}, status = 404)

class CommentView(View):
    def get(self, request):
        return JsonResponse({'comment':[]}, status=200)

class PostReviewView(View):
    def get(self, request):
        posts = Post.objects.order_by('?')[:7]
        review = [
                  {'id'    : post.id,
                   'title' : post.title,
                   'image' : post.first_image,
                   'likes' : post.like_number,
                   'views' : post.view_number
        } for post in posts]
        return JsonResponse({'reviews': list(review)}, status = 200)

        return HttpResponse(status = 404)
