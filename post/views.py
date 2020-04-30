import json
import datetime

from .models    import Post, PostComment

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

        return JsonResponse({'message': 'POST_DOES_NOT_EXIST'}, status = 404)

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
        return JsonResponse({'message': "Success"}, status = 200)

