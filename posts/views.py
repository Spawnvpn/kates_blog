from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from posts.models import BlogPost


class BlogPostListView(ListView):
    template_name = 'index.html'
    model = BlogPost
    context_object_name = 'posts_list'

    def post(self, request, **kwargs):
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')
        image = request.FILES.get('image', '')
        BlogPost.objects.create(title=title, text=text, image=image)
        return redirect('/')

    def get_queryset(self):
        qs = BlogPost.objects.filter().order_by('-pk')
        return qs


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'update-post.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('posts')

