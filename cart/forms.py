from django import forms


class AddToCartForm(forms.Form):
    QUANTITY_LIST = [(i, str(i)) for i in range(1, 31)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_LIST, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
