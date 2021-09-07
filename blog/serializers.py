from rest_framework import serializers

from .models import Projects, News, Event, Slider1, Slider2, Slider3


class ProjectsListSerializer(serializers.ModelSerializer):
    """СПИСОК ПРОЕКТОВ"""

    class Meta:
        model = Projects
        fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    """СПИСОК МЕРОПРИЯТИЙ"""

    class Meta:
        model = Event
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class NewsListSerializer(serializers.ModelSerializer):
    """СПИСОК НОВОСТЕЙ"""

    class Meta:
        model = News
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.news.__class__(value, context=self.context)
        return serializer.data


class Slider1Serializer(serializers.ModelSerializer):
    project = ProjectDetailSerializer()

    class Meta:
        model = Slider1
        fields = ('project',)


class Slider2Serializer(serializers.ModelSerializer):
    news = NewsDetailSerializer()

    class Meta:
        model = Slider2
        fields = ('news',)


class Slider3Serializer(serializers.ModelSerializer):
    event = EventDetailSerializer()

    class Meta:
        model = Slider3
        fields = ('event',)
