from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .forms import *
from .models import Post


class HomePost(ListView):
    paginate_by = 1
    model = Post
    ordering = '-created'
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


# @login_required(login_url='/login/')
# def create_post(request):
#     form = PostForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save(commit=False)
#             form.author = request.user.username
#             form.save()
#             redirect('blog:index')
#
#     return render(request, 'create_post.html', {'form': form})

class CreatePost(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('blog:login')
    form_class = PostForm
    template_name = 'create_post.html'
    extra_context = {'title': 'Create Post'}

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author_id = request.user.pk
        post.save()
        return redirect("blog:index")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('blog:login')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('blog:index')


class UpdatePost(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    login_url = reverse_lazy('blog:login')
    model = Post
    template_name = 'update_post.html'
    extra_context = {'title': 'Update Post'}
    fields = ('title', 'content', 'avatar', 'draft', 'category')


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('blog:login')
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(data=request.POST)
        post = Post.objects.get(pk=pk)
        form.instance.post = post
        form.save()
        return redirect("blog:index")


class DeletePost(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    login_url = reverse_lazy('blog:login')
    template_name = "post_confirm_delete.html"
    model = Post
    success_url = reverse_lazy('blog:index')
    context_object_name = 'posts'
    extra_context = {'title': 'Delete Post'}

    # def test_func(self):
    #     user = self.request.user.pk
    #     post = Post.objects.get(author=user)
    #     if post.author != user:
    #         return False
    #     return True

    def test_func(self):
        obj = self.get_object()
        return obj.author_id == self.request.user.pk


class UserDetailView(DetailView):
    template_name = 'user_details.html'
    model = User
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('user', kwargs={'pk': self.object.pk})
