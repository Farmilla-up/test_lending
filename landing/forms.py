from django import forms
from django.core.exceptions import ValidationError
from django.forms import CharField

from landing.models import BaseModel


class ContactForm(forms.ModelForm):
    class Meta :
        model = BaseModel
        fields = ['name', 'email', 'message']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].isdigit():
            raise ValidationError('Имя не должно начинаться с цифры')
        return name

    def clean_message_more(self):
        message = self.cleaned_data['message']
        if len(message) > 2000:
            raise ValidationError('Сообщение должно содержать до 500 символов')
        return message
