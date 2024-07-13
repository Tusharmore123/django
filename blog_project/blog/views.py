
from distutils.command.build_scripts import first_line_re
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
from django.http import HttpResponse

from .models import Post


posts=[{
    "author":"tushar more",
    "title":"blog 1",
    "content":"content for blog 1",
    "published_date":"11/12/13"
}]
def home(request):
    # return HttpResponse("<h1>Home</h1>")

    # in django variables are passed as a conrext i.e it is passed as key value pair
    context={
        'posts':Post.objects.all(),
        'title':" Home"
    }
    
    # in django render looks for templates in app 
    # and to make it look we need to add app into intsalled_apps in settings.py in project
    # in templates you can access these value from the keys
    return render(request,"blog/home.html",context)


def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request,"blog/about.html",{'title':'about'})

class createListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-published_date']
    paginate_by=2
class addPostView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form) :
        form.instance.author=self.request.user
        return super().form_valid(form)
    

class updatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['title', 'content']


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author=self.request.user

        return super().form_valid(form)
    

    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user: # type: ignore
            return True
        return False
    

class deletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user: # type: ignore
            return True
        return False


class postDetailView(DetailView):
    model=Post