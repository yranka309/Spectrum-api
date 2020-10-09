from django.urls import path,include
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import (
    LoginView,LogoutView,PasswordResetView,
    PasswordResetDoneView,PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse
from django.conf import urls


urlpatterns=[
    path('rating',views.rating,name='rating'),
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('google_signin',views.googleSignin,name='googleSignin'),
    path('register',views.register,name='register'),
    path('loginu',views.loginu,name='login'),
    path('logout',views.logout),
    path('eventregister',views.eventregister,name='eventregister'),
    path('verify',views.verify,name='verify'),
    path('password_reset',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_done',PasswordResetDoneView.as_view(),name="password_reset_done"),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
  
]