from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views

from project.views import front, signup
from project.meowing.views import meowing
from project.meowprofile.views import meowerprofile, follow_meower, unfollow_meower, followers, follows, edit_profile

from project.meowing.api import api_add_meow

urlpatterns = [
    #
    #

    path('', front, name='front'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='LogIn.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    #
    #


    path('meowing/', meowing, name='meowing'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/', meowerprofile, name='meowerprofile'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follow/', follow_meower, name='follow_meower'),
    path('u/<str:username>/unfollow/', unfollow_meower, name='unfollow_meower'),

    #
    # API

    path('api/add_meow/', api_add_meow, name='api_add_meow'),

    # Admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
