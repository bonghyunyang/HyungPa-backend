import json
import datetime

from .models    import Post

from django.views       import View
from django.http        import HttpResponse, JsonResponse

class PostDetailView(View):
    def get(self, request, post_id):
        if Post.objects.filter(id = post_id).exists():
            post = Post.objects.get(id = post_id)
            post_attribute = {
                              'title': post.title,
                              'description': post.description,
                              'like': post.like_number,
                              'view': post.view_number,
	    }
            return JsonResponse({'post': post_attribute}, status = 200)

        return JsonResponse({'message': 'POST_DOES_NOT_EXIST'}, status = 404)

#class PostView(View):
     #def get(self, request, post_id):
