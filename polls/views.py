from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,  render

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
		}
   	 return render(request, 'polls/index.html', context)
def detail(request, question_id):
	try:
		#question= Question.objects.get(pk=question_id)
		question = get_object_or_404(Question, pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})
#	return HttpResponse("affichons cette question %s." % question_id)
def results(request, question_id):
	response = "affichons les resultats de cette question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("votons pour une question %s." % question_id)

