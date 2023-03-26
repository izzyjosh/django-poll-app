from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=100)
    def __str__(self):
        return self.question


class Option(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	options = models.CharField(max_length=50)
	
	def __str__(self):
		return self.options
		

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer = models.CharField(max_length=50)
	user_answer = models.CharField(max_length=50, blank=True)
	
	def __str__(self):
		return self.user_answer