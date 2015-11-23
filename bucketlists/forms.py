from django import forms
from django.forms import ModelForm, Textarea, TextInput, RadioSelect
from .models import BucketList


class BucketListForm(ModelForm):
    

    class Meta:
        COLORS = [('success', 'green'), ('default', 'gray'),
              ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),('info','light-blue')]
        model = BucketList
        fields = ['name', 'description', 'color']
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'BucketList Description'}),
            'name': TextInput(attrs={
                'placeholder': 'Enter A name for Your bucketlist',
                'autocomplete': 'off',
                'class': 'form-control'
            }),

            'color': RadioSelect(choices=COLORS,attrs={'class':'radio-inline',}),
        }
