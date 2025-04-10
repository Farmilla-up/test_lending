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


