from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView, DeleteView

from .models import Post, Comment

from .forms import PostForm, CommentForm
from user.models import User

from blog.models import Blog


class PostView(View):
    template_name = 'post_index.html'

    def get(self, request, pk=None):
        if pk is None:
            posts = Post.objects.all()
            return render(request, self.template_name, {'posts': posts})
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.all().filter(post=post)
        return render(request, 'post_detail.html', {'post': post,
                                                    'comments': comments})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        anon_user = User.objects.get(username='Anon')
        anon_blog = Blog.objects.get(pk=request.POST.dict().get('blog', ''))

        anon_form_data = request.POST.copy()
        anon_form_data.update({'user': anon_user,
                               'blog': anon_blog,
                               'id': Post.objects.count() + 1})

        anon_form_data.pop('csrfmiddlewaretoken')
        if form.is_valid():
            new_post = Post(**anon_form_data.dict())
            new_post.save()
            return HttpResponseRedirect(f'/posts/{anon_form_data.get("id")}')
    anon_form_data = PostForm()
    return render(request, 'create_post.html', {'form': anon_form_data})


class CommentCreateFormView(FormView, CreateView):
    model = Comment
    template_name = 'create_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('Success')
            anon_comment_data = {'id': Comment.objects.count() + 1,
                                 'content': request.POST.dict().get('content', ''),
                                 'post': Post.objects.get(pk=kwargs["pk"])}
            new_comment = Comment(**anon_comment_data)
            new_comment.save()
            return HttpResponseRedirect(f'/posts/{kwargs["pk"]}')
        args = {'form': form}
        return render(request, 'create_comment.html', args)

    def get(self, request, *args, **kwargs):
        anon_form_data = CommentForm()
        return render(request, 'create_comment.html', {'form': anon_form_data})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        post = self.object.post
        return f'/posts/{post.pk}'
