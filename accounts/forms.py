from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    model = User
    fields = ('username','email','password1','password2')