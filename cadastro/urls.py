from django.urls import path
from .views import signup

urlpatterns = [
    #path('login/'),
    path('signup/', signup, name='signup'),
]
