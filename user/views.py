import json
import datetime

from .models    import User

from django.views       import View
from django.http        import HttpResponse, JsonResponse

class PostUserView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            result          = dict()
            result['image'] = user.profile_image,
            result['name']  = user.nickname,
            result['skin']  = (user.skintone.name, user.skintype.name)
            return JsonResponse({'result':result}, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message':'invalid_user'}, status = 401)
