from django.contrib import admin
from django import forms

from naturalapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'image': 'Product Image',
        }
        help_texts = {
            'name': 'Enter the name of the product',
            'description': 'Enter the description of the product',
            'price': 'Enter the price of the product',
            'image': 'Upload the image of the product',
        }
        error_messages = {
            'name': {
                'required': 'Please enter the name of the product',
                'max_length': 'The name of the product must be less than 100 characters',
            },
            'description': {
                'required': 'Please enter the description of the product',
            },
            'price': {
                'required': 'Please enter the price of the product',
            },
            'image': {
                'required': 'Please upload the image of the product',
            },
        }
        required = {
            'name': True,
            'description': True,
            'price': True,
            'image': True,
        }
        initial = {
            'name': 'Enter the name of the product',
            'description': 'Enter the description of the product',
            'price': 'Enter the price of the product',
            'image': 'Upload the image of the product',
        }

        disabled = {
            'name': False,
            'description': False,
            'price': False,
            'image': False,
        }
        localize = {
            'name': True,
            'description': True,
            'price': True,
            'image': True,
        }

        label_suffix = {
            'name': ':',
            'description': ':',
            'price': ':',
            'image': ':',
        }
        empty_value = {
            'name': 'Enter the name of the product',
            'description': 'Enter the description of the product',
            'price': 'Enter the price of the product',
            'image': 'Upload the image of the product',
        }
        error_css_class = 'error'
        required_css_class = 'required'
        max_length = {
            'name': 100,
            'description': 1000,
            'price': 100,
            'image': 100,
        }
        min_length = {
            'name': 3,
            'description': 10,
            'price': 1,
            'image': 1,
        }
        strip = {
            'name': True,
            'description': True,
            'price': True,
            'image': True,
        }

        empty_permitted = {
            'name': True,
            'description': True,
            'price': True,
            'image': True,
        }
        use_required_attribute = {
            'name': True,
            'description': True,
            'price': True,
            'image': True,
        }

        widget_attrs = {
            'name': {'class': 'form-control'},
            'description': {'class': 'form-control'},
            'price': {'class': 'form-control'},
            'image': {'class': 'form-control'},
        }

        help_text_html = {
            'name': 'Enter the name of the product',
            'description': 'Enter the description of the product',
            'price': 'Enter the price of the product',
            'image': 'Upload the image of the product',
        }
        label_suffix = {
            'name': ':',
            'description': ':',
            'price': ':',
            'image': ':',
        }
