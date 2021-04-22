from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField('The Text of the Question', max_length=200)
    pub_date = models.DateTimeField('Date published')

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