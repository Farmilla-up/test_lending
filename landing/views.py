from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import BaseModel


# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            BaseModel.objects.create(**form.cleaned_data)
            return render(request, 'landing/index.html', {'form' : ContactForm, 'success' : True})
        else :
            return render(request, 'landing/index.html', {'form' : form} )

    else :
        form = ContactForm()
    return render(request, 'landing/index.html', {'form' : form })


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