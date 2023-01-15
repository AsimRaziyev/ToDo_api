from rest_framework import serializers
from webapp.models import Task


class TaskModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "deadline", "performed")


class TaskAllModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "deadline", "performed")


class TaskCreatModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "deadline")
