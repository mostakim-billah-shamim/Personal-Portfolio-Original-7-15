from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = TestimonialModel
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    