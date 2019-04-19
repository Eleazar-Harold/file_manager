import time

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from .forms import PhotoForm
from .models import Photo


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(photos_list, 5)
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(photos_list, 5)
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return render(self.request, 'photos/progress_bar_upload/index.html', {'photos': photos})

    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(photos_list, 5)
        try:
            photos = paginator.page(page)
        except PageNotAnInteger:
            photos = paginator.page(1)
        except EmptyPage:
            photos = paginator.page(paginator.num_pages)
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'photos': photos})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))


def clear_single_image(request, pk):
    if pk:
        photo = get_object_or_404(Photo, id=pk)
        photo.file.delete()
        photo.delete()
    return redirect('photos:basic_upload')
