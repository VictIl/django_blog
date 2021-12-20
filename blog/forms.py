from django import forms
from django.core.exceptions import ValidationError
from .models import *

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].empty_label = "--not specified--"

    class Meta:
        model=Movie
        fields=['title','quote','content','img','is_published','rating']
        widgets = {
            'title': forms.TextInput(attrs={'cols': 40, 'rows': 4,'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
             'quote': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 100:
            raise ValidationError('Quit playing,less symbols!')
        return title
 
    def clean_content(self):
        content = self.cleaned_data['content']

        if len(content) < 10:
            raise ValidationError('Think harder!')


        return content

        
#f = AddPostForm(request.POST, request.FILES, instance = Movie)??



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password again,please', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
     username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))    
     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
