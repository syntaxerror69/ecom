from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Address

class RegisterForm(UserCreationForm):
      first_name =forms.CharField( max_length=200, required=False)
      last_name =forms.CharField( max_length=200, required=False)
      email = forms.EmailField()

#      class Meta:
#       model = Register
#       fields = '__all__'

# class Login(ModelForm):
    
#     class Meta:
#         model = Login
#         fields = '__all__'

class AddressForm(forms.ModelForm):
      class Meta:
            model = Address
            exclude = ('user',)
