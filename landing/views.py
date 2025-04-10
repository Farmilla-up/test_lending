from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import BaseModel
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо! Заявка отправлена.')
            return redirect('home')
        else:

            return render(request, 'landing/index.html', {
                'form': form,
                'success': False
            })
    else:

        form = ContactForm()
        return render(request, 'landing/index.html', {'form': form})


# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid() :
#             # just_created = FirstApp.objects.create(**form.cleaned_data)
#             just_created = form.save()
#             return redirect(just_created)
#     else :
#         form = PostForm()
#         return render(request, 'news/add_post.html', {'form' : form})