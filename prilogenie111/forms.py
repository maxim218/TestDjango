from django import forms
from .models import MyFirstModel

class MyForm_1(forms.ModelForm):
    class Meta:
        model = MyFirstModel
        fields = ('title', 'text', 'my_field_1', 'my_field_2', 'my_field_3', 'my_field_4')