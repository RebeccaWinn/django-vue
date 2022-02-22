from django.shortcuts import render
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)
# from django.http import HttpResponse

# posts = [
#     {
#         'author':'user1',
#         'title': 'Test title',
#         'content':'test post content',
#         'date_posted':'Feb 2, 2022',
#     },
#     {
#         'author':'user2',
#         'title': 'Test title2',
#         'content':'test post content2',
#         'date_posted':'Feb 5, 2022',
#     }   
# ]

def Index(request):
    #render template 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts.html',context)

class PostListView(ListView):
    model = Post 
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    ordering = ['date_posted']
    
class PostDetailView(DetailView):
    model = Post  

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post  
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'posts/about.html')