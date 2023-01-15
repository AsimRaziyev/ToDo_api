from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

# Create your views here.
from webapp.models import Task
from api_v1.serializers import TaskModelsSerializer, TaskAllModelsSerializer, TaskCreatModelsSerializer
from rest_framework.permissions import IsAuthenticated


class TaskView(APIView):
    serializer_class = TaskCreatModelsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer_obj = TaskModelsSerializer(instance=tasks, many=True)
        return Response(serializer_obj.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TaskDetail(APIView):
    serializer_class = TaskAllModelsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, pk, **kwargs):
        try:
            task = Task.objects.get(pk=pk)
            task_data = self.serializer_class(task).data
            return Response(task_data)
        except:
            return Response({
                "message": "Task not found."
            }, status=404)

    def put(self, request, *args, pk, **kwargs):
        try:
            task = get_object_or_404(Task, pk=pk)
            serializer = self.serializer_class(data=request.data, instance=task)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({
                "message": "Task not found."
            }, status=404)

    def delete(self, request, *args, pk, **kwargs):
        try:
            task = get_object_or_404(Task, pk=pk)
            task.delete()
            return Response({
                "message": "Task `{}` deleted.".format(pk)
            }, status=204)
        except:
            return Response({
                "message": "Task not found."
            }, status=404)


class TaskExecute(APIView):
    serializer_class = TaskAllModelsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, pk, **kwargs):
        try:
            task = Task.objects.get(pk=pk)
            task.performed = True
            task.save()

            # Send email

            return Response({
                "message": "Task performed.".format(pk)
            }, status=204)
        except:
            return Response({
                "message": "Unable to update performed status"
            }, status=500)
