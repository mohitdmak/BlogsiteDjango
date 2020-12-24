from django.shortcuts import render, redirect
from .form import UserRegisterForm, UserUpdateForm, UserPicUpdateForm
from django.contrib.auth.decorators import login_required
from Blog.views import home
from django.contrib import messages
from django.contrib.auth.models  import User
from .models import FollowList
from Blog.models import Post

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'ACCOUNT IS SUCCESSFULLY CREATED FOR {username} !!! YOU CAN LOGIN NOW')
            return redirect('LOGIN')
    else:
        form=UserRegisterForm
    return render(request,'Users/register.html',{'Form':form})


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=UserPicUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request,f'CONGRATS {username} !, YOUR PROFILE INFO IS UPDATED!')
            return redirect("blog-home")
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=UserPicUpdateForm(instance=request.user.profile)
        context={'u_form':u_form,'p_form':p_form}
    return render(request,'Users/profile.html',context)
    

def seeprofile(request,**kwargs):
    usr=User.objects.filter(id=kwargs['pk'])
    if request.user==usr[0]:
        return render(request,"Users/seeprofile.html",{'usr':usr[0],'fl1':False,'fl2':False,'fl3':False})
    for fl in request.user.followings.all():
        if fl.usr==usr[0]:
            return render(request,"Users/seeprofile.html",{'usr':usr[0],'fl1':True,'fl2':False,'fl3':False})
    return render(request,"Users/seeprofile.html",{'usr':usr[0],'fl2':True,'fl1':False,'fl3':False})


def follow(request,**kwargs):
    usertofollow=User.objects.filter(id=kwargs['pk'])[0]
    messages.success(request,f'You are now following {usertofollow.username} :)')
    request.user.followings.create(usr=usertofollow)
    return redirect("blog-home")


def unfollow(request,**kwargs):
    usertoremove=User.objects.filter(id=kwargs['pk'])[0]
    for fl in request.user.followings.all():
        if fl.usr==usertoremove:
            fl.delete()
    messages.success(request,f'You have successfully unfollowed { usertoremove.username } :(')
    return redirect('blog-home')


def followinglist(request):
    return render(request,"Users/followinglist.html",{'flist':request.user.followings.all()})


def myfeed(request):
    return render(request,"Users/myfeed.html",{'usr':request.user,'flist':request.user.followings.all()})
#in this html in line6, fl.usr.Post.all() didnt work , Parsing error, and fl.usr.Post would ofc not work. Note fl.usr.Post.all worked.
