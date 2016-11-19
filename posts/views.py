from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView
from rest_framework.reverse import reverse_lazy
from posts.models import BlogPost


class BlogPostListView(ListView):
    template_name = 'index.html'
    model = BlogPost
    context_object_name = 'posts_list'

    def post(self, request, **kwargs):
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')
        BlogPost.objects.create(title=title, text=text)
        return redirect('/')

    def get_queryset(self):
        qs = BlogPost.objects.filter().order_by('-pk')
        return qs


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts')
