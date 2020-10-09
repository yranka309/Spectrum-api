from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile,Event,UserToken,Registration,EventRules,RegistrationManagement
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
import random
import json

# Create your views here.
def home(request):
        return redirect('/web')

class Register(APIView):
    permission_classes=(permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('google_id')
        admission=request.POST.get('admission')
        name=request.POST.get('name')
        password=request.POST.get('password')
        branch=request.POST.get('branch')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        if User.objects.filter(username=username).count()!=0:
                return JsonResponse({'details':'User Already Exist'})
        user=User.objects.create_user(username=username,email=email,password=password,first_name=admission)
        user.save()
        login(request,user)
        y=UserProfile.objects.get(user=request.user)
        y.name=name
        y.phone=phone
        y.branch=branch
        y.admission=admission
        y.email=email
        y.save()


        token=Token.objects.create(user=user)

        return JsonResponse({'error':'false','message':'User Registered','token':token.key})

class ChangePassword(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        user=get_object_or_404(User,username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()
        return JsonResponse({'details':'Password has been changed successfully.'})

class Login(generics.CreateAPIView):
    permission_classes=(permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('admission')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is None:
            return JsonResponse({'token':'null'})
        login(request,user)
        token=Token.objects.get(user=request.user)
        user=request.user
        ee=UserProfile.objects.filter(user=request.user).count
        tn=UserToken.objects.filter(user=request.user).count
        if ee==0:
            UserProfile.objects.create(user=request.user)
        if tn==0:
            UserToken.objects.create(user=request.user)

        user_profile=UserProfile.objects.get(user=request.user)
        event_tokens=UserToken.objects.get(user=request.user)
        return JsonResponse({
            'user_info':{
                'name':user_profile.name,
                'branch':user_profile.branch,
                'coins':user_profile.coins,
                'phone':user_profile.phone,
                'admission':user_profile.admission
            },
            'event_tokens':{
                'aaviskar':event_tokens.aaviskar,
                'pubg':event_tokens.pubg,
                'sherlocked':event_tokens.sherlocked,
                'marketing_roadies':event_tokens.marketing_roadies,
                'treasure_hunt':event_tokens.treasure_hunt,
                'auction_villa':event_tokens.auction_villa,
                'cs_go':event_tokens.cs_go,
                'placement_fever':event_tokens.placement_fever,
                'laser_maze':event_tokens.lazer_maze,
                'robo_soccer':event_tokens.robo_soccer,
                'buffet_money':event_tokens.buffet_money,
                'codee':event_tokens.codee,
                'technovation':event_tokens.technovation,
                'guest_lecture':event_tokens.guest_lecture
            },
            'token':token.key,
            'teams':{
                'aaviskar':'',
                'pubg':'',
                'sherlocked':'',
                'marketing_roadies':'',
                'treasure_hunt':'',
                'auction_villa':'',
                'cs_go':'',
                'placement_fever':'',
                'laser_maze':'',
                'robo_soccer':'',
                'buffet_money':'',
                'codee':'',
                'technovation':'',
                'guest_lecture':''
            },
        })


class VerifyToken(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        event=request.POST.get('event')
        coupon=request.POST.get('coupon')
        print(coupon,event)
        if event=='pubg':
                x=request.user.usertoken.pubg
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.pubg='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='sherlocked':
                x=request.user.usertoken.sherlocked
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.sherlocked='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='marketing_roadies':
                x=request.user.usertoken.marketing_roadies
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.marketing_roadies='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='treasure_hunt':
                x=request.user.usertoken.treasure_hunt
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.treasure_hunt='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='auction_villa':
                x=request.user.usertoken.auction_villa
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.auction_villa='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='cs_go':
                x=request.user.usertoken.cs_go
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.cs_go='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='placement_fever':
                x=request.user.usertoken.placement_fever
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.placement_fever='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='laser_maze':
                x=request.user.usertoken.lazer_maze
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.lazer_maze='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='robo_soccer':
                x=request.user.usertoken.robo_soccer
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.robo_soccer='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='buffet_money':
                x=request.user.usertoken.buffet_money
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.buffet_money='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='codee':
                x=request.user.usertoken.codee
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.codee='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='technovation':
                x=request.user.usertoken.technovation
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.technovation='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='aaviskar':
                x=request.user.usertoken.aaviskar
                print(x)
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.aaviskar='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

        if event=='guest_lecture':
                x=request.user.usertoken.guest_lecture
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.guest_lecture='1'
                        t.save()
                        return JsonResponse({'details':'Success'})
                else:
                        return JsonResponse({'details':'Wrong'})

class GetData(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    def get(self,request,*args,**kwargs):
        user=request.user
        eventa=Event.objects.all().values('name')
        json_events=json.dumps(list(eventa))
        #events = serializers.serialize('json', list(eventa), fields=('name'))
        tokena=UserToken.objects.filter(user=user).values('aaviskar','technovation','codee','buffet_money','robo_soccer','lazer_maze','placement_fever','cs_go','auction_villa','treasure_hunt','marketing_roadies','sherlocked','pubg','guest_lecture')
        json_tokens=json.dumps(list(tokena))
        #tokens = serializers.serialize('json', list(tokena), fields=('event1','event2','event3','event4','event5','event6','event7','event8','event9','event10','event11','event12','event13','event14'))
        userinfoa=UserProfile.objects.filter(user=user).values('name','admission','branch','phone','coins','user_id')
        json_userinfo=json.dumps(list(userinfoa))
        #userinfo = serializers.serialize('json', list(userinfoa), fields=('name','admission','branch','phone','coin'))
        """ return JsonResponse({
            'events':events,
            'tokens':tokens,
            'userinfo':userinfo
        }) """

        return Response({'user_info':json_userinfo,'user_tokens':json_tokens,'events':json_events})

class ERegister(generics.CreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        team_name=request.POST.get('team_name')
        team_name=str(team_name)
        ad=request.POST.get('adm')
        event=request.POST.get('event')
        event=str(event)

        try:
            e=RegistrationManagement.objects.get(team_name=team_name,current_event=event).members.count()
        except RegistrationManagement.DoesNotExist:
            e=None
        print(e)
        #return Response({'message':'Testing passed'})
        if ad == 'none' and team_name!='none':
            try:
                e=RegistrationManagement.objects.get(team_name=team_name,current_event=event).members.count()
            except RegistrationManagement.DoesNotExist:
                e=None
            if e is None:
                return JsonResponse({'message':'Registration has been closed.for any queries contact co-ordinators.'})
                y=UserProfile.objects.get(user=request.user)
                RegistrationManagement.create_team(event,team_name,request.user,y.admission,y.phone,event)
            else:
                return JsonResponse({'message':'Team is Already Registered for this event'})
        elif team_name!='none' :
            #RegistrationManagement.join_team(request.user,team_name)
            if e is None:
                return JsonResponse({'message':'Registration has been closed.for any queries contact co-ordinators.'})
                #return JsonResponse({'message':'This team is not created for this event'})
            elif e<5:
                RegistrationManagement.join_team(event,team_name,request.user)
            else :
                return JsonResponse({'message':'Team is Full'})
        elif team_name=='none':
                return JsonResponse({'message':'Registration has been closed.for any queries contact co-ordinators.'})

        x=random.randint(999,99999)*67
        events=Event.objects.all()
        regi=UserToken.objects.get(user=request.user)
        if event=='aaviskar':
                if regi.aaviskar=='0':
                        regi.aaviskar=x
                else:
                        return JsonResponse({'message':'Registered in event aaviskar'})
        if event=='technovation':
                if regi.technovation=='0':
                        regi.technovation=x
                else:
                       return JsonResponse({'message':'Registered in event technovation'})
        if event=='codee':
                if regi.codee=='0':

                        regi.codee=x
                else:
                        return JsonResponse({'message':'Registered in event codee'})
        if event=='pubg':
                if regi.pubg=='0':
                        regi.pubg=x
                else:
                        return JsonResponse({'message':'Registered in event pubg'})
        if event=='sherlocked':
                if regi.sherlocked=='0':
                        regi.sherlocked=x
                else:
                        return JsonResponse({'message':'Registered in event sherlocked'})
        if event=='marketing_roadies':
                if regi.marketing_roadies=='0':
                        regi.marketing_roadies=x
                else:
                        return JsonResponse({'message':'Registered in event marketing_roadies'})
        if event=='treasure_hunt':
                if regi.treasure_hunt=='0':
                        regi.treasure_hunt=x
                else:
                        return JsonResponse({'message':'Registered in event treasure_hunt'})
        if event=='auction_villa':
                if regi.auction_villa=='0':
                        regi.auction_villa=x
                else:
                        return JsonResponse({'message':'Registered in event auction_villa'})
        if event=='cs_go':
                if regi.cs_go=='0':
                        regi.cs_go=x
                else:
                        return JsonResponse({'message':'Registered in event cs_go'})
        if event=='placement_fever':
                if regi.placement_fever=='0':
                        regi.placement_fever=x
                else:
                        return JsonResponse({'message':'Registered in event placement_fever'})
        if event=='laser_maze':
                if regi.lazer_maze=='0':
                        regi.lazer_maze=x
                else:
                        return JsonResponse({'message':'Registered in event lazer_maze'})
        if event=='robo_soccer':
                if regi.robo_soccer=='0':
                        regi.robo_soccer=x
                else:
                        return JsonResponse({'message':'Registered in event robo_soccer'})
        if event=='buffet_money':
                if regi.buffet_money=='0':
                        regi.buffet_money=x
                else:
                        return JsonResponse({'message':'Registered in event bull_stock'})
        if event=='guest_lecture':
                if regi.guest_lecture=='0':
                        regi.guest_lecture=x
                else:
                        return JsonResponse({'message':'Registered in event guest_lecture'})

        regi.save()
        adm=UserProfile.objects.get(user=request.user)
        Registration.objects.create(event=event,team_name=team_name,admission=adm.admission,token=x)
        return JsonResponse({'message':'Registered successfully in event :'+event})