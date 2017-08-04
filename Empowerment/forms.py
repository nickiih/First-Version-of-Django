from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('First_Name', 'Last_Name', 'Country','Price_in_Dollars','Product','Product_Description')
