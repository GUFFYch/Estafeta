from pydoc_data.topics import topics
import uuid
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Tests(models.Model):
    name = models.CharField(max_length=100)  # название
    subjects = models.CharField(max_length=100) # темы
    levels = models.CharField(max_length=50) # для каких уровней
    link = models.CharField(max_length=500) # ссылка на контест
    date_stat = models.DateField(max_length=50) # дата начала теста
    date_end = models.DateField(max_length=50) # дата конца теста