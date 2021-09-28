from django.forms import forms, ModelForm

from userauth.models import Users

class Adduserform(ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password', 'name', 'last_name']
        
class Loginform(ModelForm):
    class Meta:
        pass