import json
import bcrypt
import jwt
import re

from django.views import View
from django.http  import HttpResponse,JsonResponse
from brother.settings import SECRET_KEY
from .models import User,SkinType,SkinTone
# Create your views here.

class SignUpView(View):
    
    VALIDATION = {
        'email' : lambda email : False if (
            len(re.findall(
                r"/^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i",email)) > 0 
                or len(email)) == 0 
                or User.objects.filter(email = email).exists() 
                else True,
        # (?=.*[!@#$%^&+=])
        # 'password' : lambda password : False if not re.match(r"^.*(?=^.{6,12}$)(?=.*\d)(?=.*[a-zA-Z]).*$",password) else True, 
    }
    
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            for valiname,action in self.VALIDATION.items():
                if not action(data[valiname]):
                    return JsonResponse({'message' : 'FAILED'}, status=400)
            
            hashed_pass = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            
            User(
                email               = data['email'],
                password            = hashed_pass.decode('utf-8'),
                birth_date          = data.get('birth_date',None),
                selected_agreement  = data.get('selected_agreement',None),
            ).save()
            
            return JsonResponse({'message': 'SUCCESS'},status=200)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'},status=400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email = data['email']).exists() :
                user = User.objects.get(email = data['email'])
                
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    print(bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')))
                    token = jwt.encode(
                        {'user_id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')

                    return JsonResponse({"token":token},status=200)
            return HttpResponse(status=401)

        except KeyError:
            return JsonResponse({'message':"INVALID_KEYS"},status=400)
        
class ReviewUser(View):
    def get(self, request):
        try:
            userinfodetail = [{
                "profile_img" : user.profile_image,
                'name' : user.nickname,
                "skintype" : '건성',
                "skintone" : '13호',
            }for user in User.objects.all()]
            
            return JsonResponse({'userinfo' : userinfodetail},status=200)
        except:
            return JsonResponse({'message': 'USERINFO_DOES_NOT_EXIST'}, status = 404)