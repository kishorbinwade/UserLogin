import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'E-mail'} #to change label name email to E-mail
        
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username']
        

       