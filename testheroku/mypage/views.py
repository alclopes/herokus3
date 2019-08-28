from __future__ import absolute_import, unicode_literals
import os
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import MyImage, delete_all
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def mypage(request):
    context = {}
    ok = False

    # Recupera registros da base de dados
    # myimages = MyImage.objects.order_by('-created_at')
    myimages = MyImage.objects.all()

    # Apaga registro BD de imagens que não existem
    if myimages:
        if settings.USE_S3:
            path = os.path.join(settings.MEDIA_URL, str(myimages[0].image))
            # Aqui devemos questionar para apagar pois pode apenas não ter conexão no momento.
        else:
            path = os.path.join(settings.MEDIA_ROOT, str(myimages[0].image))
            ok = os.path.isfile(path)
            if not ok:
                delete_all()
                myimages = {}

    # Valida e salva dados do upload da imagem
    context['myimages'] = myimages
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            if len(myimages) > 3:
                id = myimages[len(myimages) - 1].id
                MyImage.objects.get(pk=id).delete()
            return redirect(reverse('mypage:index'))
        else:
            context['messages'] = form.errors

    # Carrega um novo objeto form para o contexto do template
    context['form'] = ImageUploadForm()
    return render(request, 'mypage/index.html', context)


def exclude_images(request):
    context = {}
    ok = delete_all()
    if ok:
        myimages = {}
    else:
        myimages = MyImage.objects.order_by('-created_at')
    context['myimages'] = myimages
    context['form'] = ImageUploadForm()
    return render(request, 'mypage/index.html', context)
