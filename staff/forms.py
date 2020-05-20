from django import forms
from core.models import Table


MAX_CAPACITY = 32


class AddTableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('capacity', 'description', 'short_description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ----------------------field for capacity--------------------------------------
        attributes = {
            'autocomplete': 'off',
            'class': 'form-control mb-3',
        }

        self.fields['capacity'] = forms.IntegerField(min_value=1,
                                                     max_value=MAX_CAPACITY,
                                                     widget=forms.NumberInput(attrs=attributes))
        # ----------------------------------------------------------------------------------



