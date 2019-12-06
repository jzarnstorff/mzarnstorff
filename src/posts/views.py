from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Import class views for CRUD operations
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView )

# Models
from posts.models import Post


def index(request):
    return render(request, 'posts/index.html')


class PostsListView(ListView):
    paginate_by = 5

    def get_queryset(self):
        """Override the get_queryset method to dynamically filter
           objects in database based on its assigned category."""
        self.category = self.kwargs.get('category')
        choices = list(zip(*Post.category_choices))
        if self.category not in choices[0]:
            raise Http404()
        return Post.objects.filter(category=self.category)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image', 'category', 'content']
    login_url = 'login'

    def form_valid(self, form):
        """Override form_valid method to assign the user who is
           currently logged in as the author of the post."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'image', 'category', 'content']
    login_url = 'login'

    def form_valid(self, form):
        """Override form_valid method to assign the user who is
           currently logged in as the author of the post."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Only author author of the post to make changes."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    login_url = 'login'
    success_url = '/'

    def test_func(self):
        """Only author author of the post to make changes."""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

