from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
from Users.models import FollowList
from django.contrib.auth.decorators import login_required


def home(request):
    context={'post':Post.objects.all(),'followlist':user.followings.all()}
    return render(request,'Blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='Blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name='post'
    ordering=['-time']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        messages.success(self.request,'Congrats! Your Post has been Published :)')
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    template_name="Blog/post_update.html"
    fields=['title','content']
    
    def form_valid(self, form):
        if form.instance.author==self.request.user:
            messages.success(self.request,'Congrats! Your Post has been Edited :)')
            return super().form_valid(form)
        else:
            messages.error (self.request,'YOU CANNOT EDIT ANYONES POST EXCEPT YOUR OWN :(')
            return redirect('post_detail', form.instance.id)

#NOTE::: I COULD HAVE USED AN ALTERNATIVE:
#IMPORT UserPassesTestMixin 
#from django.contrib.auth.mixins, and use it as a parameter inside PostUpdateView class
# Then create a test for this parameter as follow:
#def test_func(self):
#   post=self.get_object()     (get_object is a method of the Update view )
#   if self.request.user==post.author:
#       return True
#   else:
#       return False
#as suggested in Corey Playlist

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
    

def about(request):
    return render(request,"Blog/about.html")

@login_required
def star(request,**kwargs):
    posttofollow= Post.objects.filter(id= kwargs['pk'])[0]
    request.user.Starred.create(whichpost=posttofollow)
    messages.success(request, "You have added the Post to your favourites")
    return redirect('blog-home')


