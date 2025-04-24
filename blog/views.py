from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Projects, News, Event, Slider3, Slider1, Slider2
from .serializers import ProjectsListSerializer, ProjectDetailSerializer, NewsListSerializer, EventDetailSerializer, \
    NewsDetailSerializer, EventListSerializer, Slider2Serializer, Slider3Serializer, Slider1Serializer


class ProjectListView(APIView):
    """Список проектов"""

    def get(self, request):
        project = Projects.objects.all()
        serializer = ProjectsListSerializer(project, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        project = Projects.objects.get(id=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)


class NewsListView(APIView):
    """Список новостей"""

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True, context={"request": request})
        return Response(serializer.data)


class NewsDetailView(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        project = News.objects.get(id=pk)
        serializer = NewsDetailSerializer(project, context={"request": request})
        return Response(serializer.data)


class EventListView(APIView):
    """Список проектов"""

    def get(self, request):
        project = Event.objects.all()
        serializer = EventListSerializer(project, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        project = Event.objects.get(id=pk)
        serializer = EventDetailSerializer(project)
        return Response(serializer.data)


class Slider1View(APIView):
    """Описание проекта"""

    def get(self, request):
        slider = Slider1.objects.all()
        serializer = Slider1Serializer(slider, many=True)
        return Response(serializer.data)


class Slider2View(APIView):
    """Описание проекта"""

    def get(self, request):
        slider = Slider2.objects.all()
        serializer = Slider2Serializer(slider, many=True)
        return Response(serializer.data)


class Sldier3View(APIView):
    """Описание проекта"""

    def get(self, request):
        slider = Slider3.objects.all()
        serializer = Slider3Serializer(slider, many=True)
        return Response(serializer.data)


class Slider1ViewDetail(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        slider = Slider1.objects.get(id=pk)
        serializer = Slider1Serializer(slider, many=True)
        return Response(serializer.data)


class Slider2ViewDetail(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        slider = Slider2.objects.get(id=pk)
        serializer = Slider2Serializer(slider, many=True)
        return Response(serializer.data)


class Sldier3ViewDetail(APIView):
    """Описание проекта"""

    def get(self, request, pk):
        slider = Slider3.objects.get(id=pk)
        serializer = Slider3Serializer(slider, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')


def indexPK(request, pk):
    return render(request, 'index.html')
