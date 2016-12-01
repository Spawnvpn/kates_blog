from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from photos.models import Photo


class PhotoListView(ListView):
    template_name = 'gallery.html'
    model = Photo
    context_object_name = 'photos'

    def post(self, request, **kwargs):
        image = request.FILES.get('photo', '')
        Photo.objects.create(image=image)
        return redirect('/gallery/')


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos')
