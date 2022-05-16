import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')

   # Overwrite the __str__ function from parent class
   def __str__(self):
      return self.question_text

   # How to display the pub_date field in the admin portal
   @admin.display(
      boolean=True,
      ordering='pub_date',
      description='Published recently?',
   )

   # Only show questions that are older than now()
   def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now

   

class Choice(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_text = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)

   def __str__(self):
      return self.choice_text

datetime.timedelta(days=1)