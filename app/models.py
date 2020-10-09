from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=13,default='')
    name=models.CharField(max_length=100,default='')
    branch=models.CharField(max_length=100,default='')
    coins=models.IntegerField(default=500)
    admission=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    imageurl=models.CharField(max_length=200,default='https://i.stack.imgur.com/l60Hf.png')

    def __str__(self):
        return self.admission

def create_profile(sender,**kwargs):
    if kwargs['created']:
         user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Event(models.Model):
    name=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class EventRules(models.Model):
    event=models.OneToOneField(Event,on_delete=models.CASCADE)
    about=models.CharField(max_length=1500,default='')
    rules=models.CharField(max_length=1500,default='')
    judging=models.CharField(max_length=1500,default='')
    prizes=models.CharField(max_length=1500,default='')
    contacts=models.CharField(max_length=1500,default='')

    def __str__(self):
        return self.event.name

def create_rules(sender,**kwargs):
    if kwargs['created']:
         event_rules=EventRules.objects.create(event=kwargs['instance'])

post_save.connect(create_rules,sender=Event)

class Registration(models.Model):
    event=models.CharField(max_length=100,default='')
    team_name=models.CharField(max_length=50,default='')
    admission=models.CharField(max_length=100,default='')
    token=models.CharField(max_length=20,default='0')

    

class UserToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aaviskar=models.CharField(max_length=20,default='0')
    technovation=models.CharField(max_length=20,default='0')
    codee=models.CharField(max_length=20,default='0')
    buffet_money=models.CharField(max_length=20,default='0')
    robo_soccer=models.CharField(max_length=20,default='0')
    lazer_maze=models.CharField(max_length=20,default='0')
    placement_fever=models.CharField(max_length=20,default='0')
    cs_go=models.CharField(max_length=20,default='0')
    auction_villa=models.CharField(max_length=20,default='0')
    treasure_hunt=models.CharField(max_length=20,default='0')
    marketing_roadies=models.CharField(max_length=20,default='0')
    sherlocked=models.CharField(max_length=20,default='0')
    pubg=models.CharField(max_length=20,default='0')
    guest_lecture=models.CharField(max_length=20,default='0')

    def __str__(self):
        return self.user.userprofile.admission

def create_token(sender,**kwargs):
    if kwargs['created']:
         user_token=UserToken.objects.create(user=kwargs['instance'])

post_save.connect(create_token,sender=User)

class TeamLeader(models.Model):
    team_leader=models.CharField(max_length=100,default='0')
    team_name=models.CharField(max_length=100,default='0')
    adm_no=models.CharField(max_length=100,default='0')
    phone=models.CharField(max_length=100,default='0')
    event=models.CharField(max_length=100,default='0')
    def __str__(self):
        return self.adm_no

class RegistrationManagement(models.Model):
    members=models.ManyToManyField(User)
    current_event=models.CharField(max_length=100,default='')
    team_name=models.CharField(max_length=100,default='')

    @classmethod
    def join_team(cls,current_event,team_name,current_user):
        friends,created=cls.objects.get_or_create(
            team_name=team_name,
            current_event=current_event
        )
        friends.members.add(current_user)

    @classmethod
    def create_team(cls,current_event,team_name,current_user,admission,phone,event):
        TeamLeader.objects.create(team_leader=current_user,team_name=team_name,adm_no=admission,phone=phone,event=event)
        friends,created=cls.objects.get_or_create(
            team_name=team_name,
            current_event=current_event
        )
        friends.members.add(current_user)

    def __str__(self):
        return self.team_name

class RatingModel(models.Model):
    event=models.CharField(max_length=30,default='')
    average_rating=models.CharField(max_length=20,default='0')
    number_of_rates=models.CharField(max_length=20,default='0')

    def __str__(self):
        return self.event

class UserRated(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aaviskar=models.CharField(max_length=20,default='0')
    technovation=models.CharField(max_length=20,default='0')
    codee=models.CharField(max_length=20,default='0')
    buffet_money=models.CharField(max_length=20,default='0')
    robo_soccer=models.CharField(max_length=20,default='0')
    lazer_maze=models.CharField(max_length=20,default='0')
    placement_fever=models.CharField(max_length=20,default='0')
    cs_go=models.CharField(max_length=20,default='0')
    auction_villa=models.CharField(max_length=20,default='0')
    treasure_hunt=models.CharField(max_length=20,default='0')
    marketing_roadies=models.CharField(max_length=20,default='0')
    sherlocked=models.CharField(max_length=20,default='0')
    pubg=models.CharField(max_length=20,default='0')
    guest_lecture=models.CharField(max_length=20,default='0')

    def __str__(self):
        return self.user.userprofile.admission

def create_rating(sender,**kwargs):
    if kwargs['created']:
         user_token=UserRated.objects.create(user=kwargs['instance'])

post_save.connect(create_rating,sender=User)

