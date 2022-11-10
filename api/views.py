from rest_framework.response import Response
from rest_framework import viewsets
from .models import Mood
from .serializers import MoodSerializer

class MoodViewset(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
