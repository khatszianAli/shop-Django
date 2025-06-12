from .models import Category
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'price']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'The name of a product'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'The description of a product'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'The price of a product'
            })
        }
