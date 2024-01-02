from .models import Product
from django import forms

class ProductForm(forms.Form):
    """A Django form for handling product IDs."""
    product_ids = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'cols': 30,
                'rows': 10,
                'placeholder': 'Enter your IDs, separated by commas. (Like: p-A022187663, p-A102158683, p-A048406698)'
            }
        )
    )

    def clean_product_ids(self):
        """Cleans and validates the product_ids field."""
        data = self.cleaned_data['product_ids']
        return [id.strip() for id in data.split(',')]
