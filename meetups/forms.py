from django import forms
from django import forms
# from .models import Participant

#registration of form
class RegistrationForm(forms.Form):
  email = forms.EmailField(label='Your email')
 
  
