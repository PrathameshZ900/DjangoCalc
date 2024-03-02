# forms.py

from django import forms


class CalculatorForm(forms.Form):
    OPERATORS = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ]

    Value1 = forms.IntegerField(label='Value 1')
    Operater = forms.ChoiceField(choices=OPERATORS, label='Operator')
    Value2 = forms.IntegerField(label='Value 2')
