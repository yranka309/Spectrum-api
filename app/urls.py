from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as vw
from django.conf import urls

""" router=routers.DefaultRouter()
router.register('app',views.UserProfileView) """

urlpatterns = [
   path('',views.home,name='home'),
   path('register',view=views.Register.as_view()),
   path('change_password',views.ChangePassword.as_view()),
   path('login',view=views.Login.as_view()),
   path('token_login',view=vw.obtain_auth_token),
   path('verify_token',view=views.VerifyToken.as_view()),
   path('get_data',view=views.GetData.as_view()),
   path('e_register',view=views.ERegister.as_view()),
]