from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question

def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # output = ', '.join([q.question_text for q in latest_question_list])
   # template = loader.get_template('polls/index.html')
   context = {
      'latest_question_list': latest_question_list,
   }
   return render(request, 'polls/index.html', context)
   # return HttpResponse(template.render(context, request))
   # return HttpResponse("Hello, world, You're at the polls index.")

def detail(request, question_id):
   question = get_object_or_404(Question,pk=question)
   try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
      # redisplay the question voting form
      return render(request, 'polls/detail.html', {
         'question': question,
         'error_message': "You didn't select a choice.",
      })
   else:
      selected_choice.votes =+ 1
      selected_choice.save()
      # Always return an HttpResponseRedirect after successfully dealing
      # with POST data.
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
   # return render(request, 'polls/details.html', {'question': question})

   # return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
   return HttpResponse("You're voting on question %s." % question_id)


