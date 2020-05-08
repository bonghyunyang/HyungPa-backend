import random
import json
import bcrypt
import jwt
import re
import datetime


from product.models   import *
from post.models      import *
from user.models      import *
from review.models    import *
from django.db.models import Avg

from django.views     import View
from django.http      import JsonResponse, HttpResponse
from brother.settings import SECRET_KEY


class SignUpView(View):
    VALIDATION = {
        'email': lambda email: False if (
            len(re.findall(
            r"/^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i", email)) > 0
            or len(email)) == 0
                or User.objects.filter(email=email).exists()
                else True,
        # (?=.*[!@#$%^&+=])
        # 'password' : lambda password : False if not re.match(r"^.*(?=^.{6,12}$)(?=.*\d)(?=.*[a-zA-Z]).*$",password) else True,
    }

    def post(self, request):
        data = json.loads(request.body)

        try:
            for valiname, action in self.VALIDATION.items():
                if not action(data[valiname]):
                    return JsonResponse({'message': 'FAILED'}, status=400)

            hashed_pass = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            User(
                email             = data['email'],
                password          = hashed_pass.decode('utf-8'),
                birth_date        = data.get('birth_date', None),
                selected_agreement= data.get('selected_agreement', None),
            ).save()

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    print(bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')))
                    token = jwt.encode(
                        {'user_id': user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')

                    return JsonResponse({"token": token}, status=200)
            return HttpResponse(status=401)

        except KeyError:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)

class PostUserView(View):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id = user_id)
            result = dict()
            result['image'] = user.profile_image,
            result['name'] = user.nickname,
            result['skin'] = (user.skintone.name, user.skintype.name)
            return JsonResponse({'result': result}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'invalid_user'}, status=401)

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

        reviews = Review.objects.order_by('?')[:4]
        review_home = [
            {'id': review.id,
             'first_image': review.review_image,
             'first_comment' : review.review_comment,
             'likes': review.like_number,
             'views': review.view_number
             } for review in reviews]

        posts = Post.objects.order_by('?')[:6]
        post_home = [
            {'id'          : post.id,
             'title'       : post.title,
             'first_image' : post.first_image,
             'likes'       : post.like_number,
             'views'       : post.view_number
             } for post in posts]

        return JsonResponse({'ProductData1' : product_ranking, 'Review_data2' : review_home, 'PostData3' : post_home}, status = 200)