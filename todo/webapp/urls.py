from django.contrib import admin
from django.urls import path

from webapp.views.tasks import IndexView

app_name = "webapp"

urlpatterns = [
    path("", IndexView.as_view(), name="index")

]

