from django import forms
#local
from .models import Sale


class VentaForm(forms.Form):
    barcode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Codigo de barras',
                'class': 'input-group-field',
            }
        )
    )
    count = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'input-group-field',
            }
        )
    )
    #
    def clean_count(self):
        count = self.cleaned_data['count']
        if count < 1:
            raise forms.ValidationError('Ingrese una cantidad mayor a cero')

        return count
    

class VentaVoucherForm(forms.Form):

    type_payment = forms.ChoiceField(
        required=False,
        choices=Sale.TIPO_PAYMENT_CHOICES,
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    type_invoce = forms.ChoiceField(
        required=False,
        choices=Sale.TIPO_INVOCE_CHOICES,
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )