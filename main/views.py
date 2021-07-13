from django.shortcuts import render
from .models import Resume,Skill,Project
# Create your views here.
def home(request):
	context = dict()
	resume = Resume.objects.all()
	skill = Skill.objects.all()
	project=Project.objects.all()
	context["resume"]=resume
	context["skill"]= skill
	context["project"]=project

	return render(request,'main/home.html', context = context)

def blog(request):
	return render(request, 'main/blog.html')