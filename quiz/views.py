from rest_framework.compat import INDENT_SEPARATORS
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.

@api_view(['GET'])
def helloAPI(request:HttpRequest):
	return Response('Hello World!')

@api_view(['GET'])
def randomQuiz(request, id):
	total_quizes = Quiz.objects.all()
	random_quizes = random.sample(list(total_quizes), id)
	serializer = QuizSerializer(random_quizes, many=True)
	return Response(serializer.data)
