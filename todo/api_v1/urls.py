from django.urls import path, include, re_path
from api_v1.views import TaskView, TaskDetail, TaskExecute


app_name = "api_v1"

urlpatterns = [

   path('tasks/', TaskView.as_view()),
   path('tasks/<int:pk>/', TaskDetail.as_view()),
   path('tasks/<int:pk>/execute/', TaskExecute.as_view()),
   path('auth/', include('djoser.urls')),
   re_path(r'^auth/', include('djoser.urls.authtoken')),

]
