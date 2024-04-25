from django import forms

class TipForm(forms.Form):
    bill_amount = forms.DecimalField(label='Bill Amount', max_digits=10, decimal_places=2)
    tip_percentage = forms.DecimalField(label='Tip Percentage', max_digits=5, decimal_places=2)
