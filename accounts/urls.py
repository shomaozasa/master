from django.urls import path
from . import views
app_name = 'acounts'
urlpatterns = [
    path('signup/',
         views.SginUpView.as_view(),
         name = 'signup'),
         
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
]
