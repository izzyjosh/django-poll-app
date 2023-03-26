from django.shortcuts import render, redirect
from .models import *


def welcome(request):
	
	return render(request, "welcome.html")
	
def index(request, q_id):
	
	question = Question.objects.get(id=q_id)
	questions = Question.objects.all()
	
	if request.method == "POST":
		ans = request.POST.get("option")
		print(ans)
		question.answer_set.create(user_answer=ans)
		
		return redirect("index", q_id=q_id+1)
		
		
	a = question.option_set.all()[0]
	b = question.option_set.all()[1]
	c = question.option_set.all()[2]
	d = question.option_set.all()[3]
		
	context = {
		"question":question, 
		"a":a, 
		"b":b, 
		"c":c, 
		"d":d, 
		"questions":questions, 
	}
	return render(request, "index.html", context)
	
def previous(request, q_id):
	question = Question.objects.get(id=q_id)
	return redirect("index", q_id=question.id - 1)
	

def finish(request):
	return redirect("welcome")