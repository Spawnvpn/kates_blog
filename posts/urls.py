from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from posts import views

urlpatterns = [
    # url(r'^search/$', view=views.search_view, name='search'),
    url(r'^$', view=views.BlogPostListView.as_view(), name='posts'),
    url(r'^delete-post/(?P<pk>.+)/$', view=views.BlogPostDeleteView.as_view()),
    url(r'^update-post/(?P<pk>.+)/$', view=views.BlogPostUpdateView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
