from pydoc_data.topics import topics
import uuid
from django.db import models
from django.forms import ModelForm


# Create your models here.
class Tests(models.Model):
    name = models.CharField(max_length=100)  # название
    subject = models.CharField(max_length=100) # темы
    level = models.CharField(max_length=50) # для каких уровней
    link = models.CharField(max_length=500) # ссылка на контест
    date_start = models.DateField(max_length=50) # дата начала теста
    time_start = models.TimeField(auto_now=False, auto_now_add=False) # время начала теста
    date_end = models.DateField(max_length=50) # дата конца теста
    time_end = models.TimeField(auto_now=False, auto_now_add=False) # время конца теста
    is_active = models.BooleanField(default=True) # Окончен или нет
    results_link = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True) # название
    language = models.CharField(max_length=50) # страна
    password = models.CharField(max_length=100) # пароль