from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import Account, TableBookingQueue


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except:
                return email

            raise forms.ValidationError(f'Email {email} already exist')

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except:
                return username

            raise forms.ValidationError(f'Username {username} already exist')


class BookingForm(forms.ModelForm):
    dt_start = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    dt_end = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = TableBookingQueue
        fields = ('table', 'account', 'guests_count', 'dt_start', 'dt_end')
