from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path("", TemplateView.as_view(), name="template"),
]
