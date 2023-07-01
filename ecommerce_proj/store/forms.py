from django import forms
from .models import Product, Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['description']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    