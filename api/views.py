from django.shortcuts import render
from core.models import Question, Person
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from api.serializers import PersonModelSerializer
# Create your views here.

def detail(request, pk):
    question = Question.objects.get(pk=pk)
    data = {
        "title": question.question_text
    }
    return JsonResponse(data)

@csrf_exempt
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonModelSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return JsonResponse({"message" : "not found"}, status=404)
    
    if request.method == 'GET':
        serializer = PersonModelSerializer(instance=person)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonModelSerializer(instance=person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        person.delete()
        return JsonResponse({"message": "deleted"}, status=204)
    