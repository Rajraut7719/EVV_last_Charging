
from django import forms
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm

# class RegisterForm(UserCreationForm):
#     full_name=forms.CharField(error_messages={'required':'Enter Full Name'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
#     username=forms.CharField(error_messages={'required':'Enter Username'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
#     mobile=forms.CharField(max_length=12,error_messages={'required':'Enter Mobile No'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
#     email=forms.EmailField(error_messages={'required':'Enter Email'},widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}))
#     password1=forms.CharField(error_messages={'required':'Enter password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
#     password2=forms.CharField(error_messages={'required':'Enter Conform Password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Password'}))
#     # check=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

#     class Meta:
#         model=User
#         fields=['full_name','username','mobile','email']

class RegisterForm(UserCreationForm):
    password1=forms.CharField( error_messages={'required':'Enter password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField( error_messages={'required':'Enter Conform password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Conform Password'}))
   
    class Meta:
        model=User
        fields=['full_name','username','mobile','email']
        
        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile No'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}),
            # 'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Email ID'})
        }
      

# Change Password
class Password_change_Form(PasswordChangeForm):
    old_password=forms.CharField(error_messages={'required':'Enter old Password'},widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(error_messages={'required':'Enter password'},label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(error_messages={'required':'Enter Conform password'},label='Conform Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Login_Form(AuthenticationForm):
    username=forms.CharField(error_messages={'required':'Enter Username'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(error_messages={'required':'Enter password'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
