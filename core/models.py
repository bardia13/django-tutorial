from django.db import models
from django.contrib import admin
import datetime
from django.utils import timezone
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class Question(models.Model):
    question_text = models.CharField('The Text of the Question', max_length=200)
    pub_date = models.DateTimeField('Date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='published recently'
    )
    def was_published_recently(self):
        if self.pub_date > timezone.now() - datetime.timedelta(days=1):
            return True
        else:
            return False

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
