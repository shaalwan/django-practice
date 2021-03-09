from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=300)
    publish_date = models.DateTimeField()

class Choice(models.Model):
    text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
