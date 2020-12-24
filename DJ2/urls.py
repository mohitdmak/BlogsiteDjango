"""DJ2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Users import views as Users_views
from django.conf import settings
from django.conf.urls.static import static
from Blog import views as Blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('register/',include('Users.urls')),
    path('login/',auth_views.LoginView.as_view(template_name="Users/login.html"),name="LOGIN"),
    path('logout/',auth_views.LogoutView.as_view(template_name="Users/logout.html"),name="LOGOUT"),
    path('profile/',Users_views.profile,name="PROFILE"),
    path("profile/<int:pk>/", Users_views.seeprofile , name="SEEPROFILE"),
    path("profile/<int:pk>/follow/",Users_views.follow, name="FOLLOW"),
    path("followinglist/",Users_views.followinglist,name="FOLLOWINGLIST"),
    path("profile/<int:pk>/unfollow/",Users_views.unfollow,name="UNFOLLOW"),
    path("myfeed/",Users_views.myfeed,name="MY-FEED"),
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="Users/password_reset.html"),name="passowrd_reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="Users/password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="Users/password_reset_confirm.html"),name="password_reset_confirm")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)