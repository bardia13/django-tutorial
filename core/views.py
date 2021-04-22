from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from core.models import Question


def detail(request, question_id):
    response = " Question number %s"
    return HttpResponse(response % question_id)


def result(request, question_id):
    response = " The results of Question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting for question %s" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render(context, request))


def test(request):
    template = loader.get_template('core/test.html')
    return HttpResponse(template.render({}, request))
