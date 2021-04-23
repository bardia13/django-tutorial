from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from core.models import Question, Choice
from django.urls import reverse
from django.views import generic


class DetailView(generic.DetailView):
    model = Question
    template_name = 'core/detail.html'


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question not Found!")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'core/detail.html', {"question": question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'core/result.html'

# def result(request, question_id):
#     response = " The results of Question %s"
#     return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (Choice.DoesNotExist, KeyError):
        return render(request, 'core/detail.html', {
            'question': question,
            'error_message': "Dadash Dari Eshtebah Mizani!!"
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('core:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'latest_question_list'

    def queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     # template = loader.get_template('core/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'core/index.html', context)


def test(request):
    template = loader.get_template('core/test.html')
    return HttpResponse(template.render({}, request))
