from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib import admin,auth
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
#from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver
from django.contrib.auth import login,authenticate
from app.models import UserProfile,Event,UserToken,Registration,EventRules,RegistrationManagement,RatingModel,UserRated
import random
from django.http import JsonResponse
import itertools

# Create your views here.
def home(request):
        eventa=Event.objects.all()
        events=[]
        single=['marketing_roadies','buffet_money','placement_fever']
        eee=['Sherlocked','Pubg','Roadies','Treasure Hunt','Auction Villa','Cs Go','Placement Fever','Lazer Maze','Robo Soccer','Bull Stock 2.0','Codee','Technovation','Aaviskar','Guest Lecture']
        rankers=UserProfile.objects.order_by('-coins')[:20]
        ranks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        rankersprofile=[]
        for i in rankers:
                rankersprofile.append(i)
        for ev in eventa:
                events.append(ev.name)
                print(ev.eventrules.about)

        if request.user.is_authenticated:
                rl=[]
                events=[]
                try:
                        e=UserProfile.objects.filter(user=request.user).count()
                except UserProfile.DoesNotExist:
                        UserProfile.objects.create(user=request.user)
                u=UserProfile.objects.get(user=request.user)
                try:
                        f=UserRated.objects.filter(user=request.user).count()
                        print(e)
                except UserRated.DoesNotExist:
                        UserRated.objects.create(user=request.user)
                try:
                        g=UserToken.objects.filter(user=request.user).count()
                except UserToken.DoesNotExist:
                        UserToken.objects.create(user=request.user)
                if e==0:
                        UserProfile.objects.create(user=request.user)
                if f==0:
                        UserRated.objects.create(user=request.user)
                if g==0:
                        UserToken.objects.create(user=request.user)
                t=UserToken.objects.get(user=request.user)
                tt=UserRated.objects.get(user=request.user)
                tokens=[]
                tokens.append(t.sherlocked),events.append('sherlocked'),tokens.append(t.pubg),events.append('pubg'),tokens.append(t.marketing_roadies),events.append('marketing_roadies'),tokens.append(t.treasure_hunt),events.append('treasure_hunt'),tokens.append(t.auction_villa),events.append('auction_villa'),tokens.append(t.cs_go),events.append('cs_go'),tokens.append(t.placement_fever),events.append('placement_fever')
                tokens.append(t.lazer_maze),events.append('lazer_maze'),tokens.append(t.robo_soccer),events.append('robo_soccer'),tokens.append(t.buffet_money),events.append('buffet_money'),tokens.append(t.codee),events.append('codee'),tokens.append(t.technovation),events.append('technovation'),tokens.append(t.aaviskar),events.append('aaviskar'),tokens.append(t.guest_lecture),events.append('guest_lecture')
                rl.append(tt.sherlocked),rl.append(tt.pubg),rl.append(tt.marketing_roadies),rl.append(tt.treasure_hunt),rl.append(tt.auction_villa),rl.append(tt.cs_go),rl.append(tt.placement_fever)
                rl.append(tt.lazer_maze),rl.append(tt.robo_soccer),rl.append(tt.buffet_money),rl.append(tt.codee),rl.append(tt.technovation),rl.append(tt.aaviskar),rl.append(tt.guest_lecture)
                #print(tokens)
                #print(events)
                coin=u.coins
                rp=UserProfile.objects.order_by('-coins')
                ru=0
                for x in rp:
                        ru=ru+1
                        if x.admission==request.user.userprofile.admission:
                                break
                mylist=zip(events,tokens,eventa,rl,eee)
                rppp=zip(rankersprofile,ranks)
                args={'coin':coin,'mylist':mylist,'single':single,'eventa':eventa,'ru':ru,'rppp':rppp}
                return render(request,'myapp/events.html',args)
        tokens=[5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        rl=[5,5,5,5,5,5,5,5,5,5,5,5,5,5]
        mylist=zip(events,tokens,eventa,rl,eee)
        rppp=zip(rankersprofile,ranks)
        args={'mylist':mylist,'single':single,'eventa':eventa,'rppp':rppp}
        return render(request,'myapp/events.html',args)

def register(request):
    if request.method == 'POST':
        print('process initiated')
        name=request.POST.get('id_name')
        username=request.POST.get('id_username')
        imageurl=request.POST.get('imageaurl')
        branch=request.POST.get('id_branch')
        email=request.POST.get('id_email')
        phone=request.POST.get('id_phone')
        y=UserProfile.objects.get(user=request.user)
        y.name=name
        y.phone=phone
        y.branch=branch
        y.email=email
        y.admission=username
        y.imageurl=imageurl
        y.save()
        print(name,email,imageurl)
        return HttpResponse('Success')
@login_required
def profile(request):
        user=request.user
        p=UserProfile.objects.get(user=user)
        args={'p':p}
        if request.method=="POST":
                name=request.POST.get('id_name')
                username=request.POST.get('id_admission')
                #imageurl=request.POST.get('imageaurl')
                branch=request.POST.get('id_branch')
                phone=request.POST.get('id_phone')
                print(name,username,phone,branch)
                print('saving data')
                y=UserProfile.objects.get(user=request.user)
                y.name=name
                y.phone=phone
                y.branch=branch
                y.admission=username
                #y.imageurl=imageurl
                y.save()
                return redirect('/web/')
        return render(request,'myapp/profile.html',args)

def loginu(request):
        username=request.POST.get('username')
        password=request.POST.get('id_password')

        print('initiated')
        user=authenticate(username=username,password=password)
        if user is None:
                return HttpResponse('Wrong')
        print(user)
        login(request,user)
        return HttpResponse('Success')


def logout(request):
    auth.logout(request)
    return redirect('/web/')

def eventregister(request):
        team_name=request.POST.get('team_name')
        team_name=str(team_name)
        ad=request.POST.get('adm')
        event=request.POST.get('event')
        event=str(event)
        print(ad,team_name,event)
        print(event)
        if team_name == "":
                return HttpResponse('null')

        try:
            e=RegistrationManagement.objects.get(team_name=team_name,current_event=event).members.count()
        except RegistrationManagement.DoesNotExist:
            e=None
        print(e)
        #return Response({'message':'Testing passed'})
        if ad == 'none':
            try:
                e=RegistrationManagement.objects.get(team_name=team_name,current_event=event).members.count()
            except RegistrationManagement.DoesNotExist:
                e=None
            if e is None:
                return HttpResponse('Registration has been been closed')
                y=UserProfile.objects.get(user=request.user)
                RegistrationManagement.create_team(event,team_name,request.user,y.admission,y.phone,event)
            else:
                return HttpResponse('Already')
        elif team_name!='none' :
            #RegistrationManagement.join_team(request.user,team_name)
            if e is None:
                return HttpResponse('Registration has been been closed')
                #return HttpResponse('ncreated')
            elif e<5:
                RegistrationManagement.join_team(event,team_name,request.user)
            else :
                return HttpResponse('Full')
        elif team_name=='none':
                return HttpResponse('Registration has been been closed')

        x=random.randint(999,99999)*67
        events=Event.objects.all()
        regi=UserToken.objects.get(user=request.user)
        event=str(event)
        if event=='aaviskar':
                regi.aaviskar=x
        if event=='technovation':
                regi.technovation=x
        if event=='codee':
                regi.codee=x
        if event=='pubg':
                regi.pubg=x
        if event=='sherlocked':
                regi.sherlocked=x
        if event=='marketing_roadies':
                regi.marketing_roadies=x
        if event=='treasure_hunt':
                regi.treasure_hunt=x
        if event=='auction_villa':
                regi.auction_villa=x
        if event=='cs_go':
                regi.cs_go=x
        if event=='placement_fever':
                regi.placement_fever=x
        if event=='laser_maze':
                regi.lazer_maze=x
        if event=='robo_soccer':
                regi.robo_soccer=x
        if event=='buffet_money':
                regi.buffet_money=x
        if event=='guest_lecture':
                regi.guest_lecture=x

        regi.save()
        adm=UserProfile.objects.get(user=request.user)
        Registration.objects.create(event=event,team_name=team_name,admission=adm,token=x)
        return HttpResponse('Success')

def verify(request):
        event=request.POST.get('event')
        coupon=request.POST.get('coupon')
        print(coupon,event,request.user)
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
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='sherlocked':
                x=request.user.usertoken.sherlocked
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.sherlocked='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='marketing_roadies':
                x=request.user.usertoken.marketing_roadies
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.marketing_roadies='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='treasure_hunt':
                x=request.user.usertoken.treasure_hunt
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.treasure_hunt='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='auction_villa':
                x=request.user.usertoken.auction_villa
                print(coupon)
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.auction_villa='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='cs_go':
                x=request.user.usertoken.cs_go
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.cs_go='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='placement_fever':
                x=request.user.usertoken.placement_fever
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.placement_fever='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='laser_maze':
                x=request.user.usertoken.lazer_maze
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.lazer_maze='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='robo_soccer':
                x=request.user.usertoken.robo_soccer
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.robo_soccer='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='buffet_money':
                x=request.user.usertoken.buffet_money
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.buffet_money='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='codee':
                x=request.user.usertoken.codee
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.codee='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

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
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='aaviskar':
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
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        elif event=='guest_lecture':
                x=request.user.usertoken.guest_lecture
                if str(x) == str(coupon):
                        y=UserProfile.objects.get(user=request.user)
                        z=y.coins
                        y.coins=z+100
                        y.save()
                        t=UserToken.objects.get(user=request.user)
                        t.guest_lecture='1'
                        t.save()
                        return HttpResponse('Success')
                else:
                        return HttpResponse('Wrong')

        else :
                HttpResponse('Invalid event')

def rating(request):
        event=request.POST.get('event')
        rvalue=request.POST.get('rvalue')
        rvalue=int(rvalue)
        print(rvalue,event)
        try:
                e=RatingModel.objects.get(event=event)
        except RatingModel.DoesNotExist:
                e=None
                RatingModel.objects.create(event=event)
        t=RatingModel.objects.get(event=event)
        x=float(t.average_rating)
        y=int(t.number_of_rates)
        x=str((x*y+rvalue)/(y+1))
        y=str(y+1)
        t.average_rating=x
        t.number_of_rates=y
        t.save()
        try:
                e=UserRated.objects.get(user=request.user)
        except RatingModel.DoesNotExist:
                e=None
                UserRated.objects.create(user=request.user)
        regi=UserRated.objects.get(user=request.user)
        x=str(rvalue)
        if event=='aaviskar':
                regi.aaviskar=x
        if event=='technovation':
                regi.technovation=x
        if event=='codee':
                regi.codee=x
        if event=='pubg':
                regi.pubg=x
        if event=='sherlocked':
                regi.sherlocked=x
        if event=='marketing_roadies':
                regi.marketing_roadies=x
        if event=='treasure_hunt':
                regi.treasure_hunt=x
        if event=='auction_villa':
                regi.auction_villa=x
        if event=='cs_go':
                regi.cs_go=x
        if event=='placement_fever':
                regi.placement_fever=x
        if event=='laser_maze':
                regi.lazer_maze=x
        if event=='robo_soccer':
                regi.robo_soccer=x
        if event=='buffet_money':
                regi.buffet_money=x
        if event=='guest_lecture':
                regi.guest_lecture=x
        regi.save()

        return HttpResponse('Success')

def googleSignin(request):
        print('googlesignin iniated')
        name=request.POST.get('name')
        ids=request.POST.get('id')
        imageurl=request.POST.get('imageurl')
        email=request.POST.get('email')
        print(ids,name,imageurl,email)
        user=authenticate(username=ids,password=email)
        if user is None:
                user = User.objects.create_user(username=ids, password=email, email=email)
                user.save()
                login(request,user)
                y=UserProfile.objects.get(user=request.user)
                y.name=name
                #y.phone=phone
                #y.branch=branch
                y.email=email
                #y.admission=username
                y.imageurl=imageurl
                y.save()
                return HttpResponse('Registered')
        else:
                print(user)
                login(request,user)
                yy=UserProfile.objects.filter(user=request.user).count()
                if yy==0:
                    UserProfile.objects.create(user=request.user)
                y=UserProfile.objects.get(user=request.user)
                y.name=name
                #y.phone=phone
                #y.branch=branch
                y.email=email
                #y.admission=username
                y.imageurl=imageurl
                y.save()
                return HttpResponse('Success')

