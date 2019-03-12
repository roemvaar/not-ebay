from django import forms
from django.contrib.auth.models import User
from shop.models import Product


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match!")


class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = ('seller', 'product_name', 'description', 'price')

        widgets = {
            # 'seller': forms.TextInput(attrs={'class': 'textinputclass'}),
            'product_name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'price': forms.NumberInput(attrs={'class': 'price'}),
        }
