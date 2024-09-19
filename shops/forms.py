from django import forms
from django.contrib import messages
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='', max_length=80,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'placeholder': 'نام خود را وارد کنید','style': 'width:400px;text-align:center'}))
    last_name = forms.CharField(label='', max_length=80,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید','style': 'width:400px;text-align:center'}))
    Email = forms.CharField(label='', max_length=80,
                            widget=forms.EmailInput(
                                attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید','style': 'width:400px;text-align:center'}))
    user_name = forms.CharField(label='', max_length=80,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید','style': 'width:400px;text-align:center'}))

    password1 = forms.CharField(label='', max_length=80,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'رمز عبور را وارد کنید','style': 'width:400px;text-align:center'}))
    password2 = forms.CharField(label='', max_length=80,
                                widget=forms.PasswordInput(
                                    attrs={'width': '100px', 'class': 'form-control',
                                           'placeholder': 'تکرار رمز عبور را وارد کنید','style': 'width:400px;text-align:center'}))

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError('این نام کاربری موجود است!!')
        else:
            return user_name

    def clean_Email(self):
        Email = self.cleaned_data['Email']
        if User.objects.filter(email=Email).exists():
            raise forms.ValidationError('این  ایمیل موجود است!!')

        else:
            return Email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('رمز عبور مطابقت ندارد!!')
        elif not any(i.isdigit() for i in self.cleaned_data["password2"]):
            raise forms.ValidationError("باید شامل عدد باشد")
        else:
            return password2

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'user_name', 'email', 'password1', 'password2')
