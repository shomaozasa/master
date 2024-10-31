from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class TemplateView(TemplateView):
    template_name = 'main/index.html' # 画面を表示するテンプレート名

class SignupView(TemplateView):
    template_name = 'main/signup.html'
