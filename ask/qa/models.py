from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
