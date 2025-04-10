from django.db import models
from django.db.models import TextField
from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length= 20, verbose_name = 'Имя')
    email = models.EmailField(verbose_name = 'Email')
    message = models.TextField(max_length= 200, verbose_name= 'Текст')
    created_at = models.DateTimeField(auto_now_add= True , verbose_name='Отправлено')

    class Meta :
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.name} - {self.email} '

# Create your models here.
