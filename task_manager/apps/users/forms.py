from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name',
                  'password1', 'password2')
