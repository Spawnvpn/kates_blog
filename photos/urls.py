from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from photos import views

urlpatterns = [
    # url(r'^search/$', view=views.search_view, name='search'),
    url(r'^gallery/$', view=views.PhotoListView.as_view(), name='photos'),
    url(r'^gallery/delete-photo/(?P<pk>.+)/$', view=views.PhotoDeleteView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
