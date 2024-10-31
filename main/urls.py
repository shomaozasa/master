from django.urls import path
from . import views
from .views import *

app_name = "main"
urlpatterns = [
    path("", TemplateView.as_view(), name="template"),
    path("/signup", SignupView.as_view(), name = "signup"),
]
