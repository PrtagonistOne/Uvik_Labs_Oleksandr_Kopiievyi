import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView, DeleteView, UpdateView

from .models import Post, Comment

from .forms import CommentForm


logger = logging.getLogger(__name__)


class PostView(View):
    template_name = 'post_index.html'

    def get(self, request, pk=None):
        logger.info('Posts get view')
        if pk is None:
            posts = Post.objects.all()
            return render(request, self.template_name, {'posts': posts})
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.all().filter(post=post)
        return render(request, 'post_detail.html', {'post': post,
                                                    'comments': comments})


class CommentCreateFormView(FormView, CreateView):
    model = Comment
    template_name = 'create_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        logger.info('Validating Comment form')
        return super().form_valid(form)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            logger.info('Success validate comment content')
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
        logger.info('Success delete comment')
        post = self.object.post
        return f'/posts/{post.pk}'


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name_suffix = '_update_form'
    template_name = 'comment_update_form.html'

    def get_success_url(self):
        logger.info('Success update comment')
        return f'/posts/{self.object.post.pk}'

