from django.shortcuts import render

from .models import News 
from .serializers import NewsSerializer
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-publication_date')
    serializer_class = NewsSerializer