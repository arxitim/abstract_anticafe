from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import Account, TableBookingQueue


AVERAGE_MAX_CAPACITY = 32


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
    class Meta:
        model = TableBookingQueue
        fields = ('table', 'account', 'guests_count', 'dt_start', 'dt_end')
        widgets = {
            'table': forms.HiddenInput(),
            'account': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        if 'custom_values' in kwargs:
            custom_values = kwargs.pop('custom_values')
            max_capacity = custom_values['max_capacity']
        else:
            max_capacity = AVERAGE_MAX_CAPACITY
        super().__init__(*args, **kwargs)

        # ----------------------field for guests count--------------------------------------
        self.fields['guests_count'] = forms.IntegerField(min_value=1,
                                                         max_value=max_capacity)
        self.fields['guests_count'].label = 'Кол-во гостей'
        # ----------------------------------------------------------------------------------

        # --------------  field for datetime of booking start ------------------------------
        attributes = {
            'autocomplete': 'off',
            'class': 'dt_start',
            'readonly': None,
        }

        self.fields['dt_start'] = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                                                      widget=forms.TextInput(attrs=attributes))
        self.fields['dt_start'].label = 'Дата и время начала посещения'
        # ----------------------------------------------------------------------------------

        # --------------  field for datetime of booking end   ------------------------------
        attributes = {
            'autocomplete': 'off',
            'class': 'dt_end',
            'readonly': None,
        }
        self.fields['dt_end'] = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                                                    widget=forms.TextInput(attrs=attributes))
        self.fields['dt_end'].label = 'Дата и время конца   посещения'
        # ----------------------------------------------------------------------------------
