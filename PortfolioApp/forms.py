from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id' : 'contact-name', 'class' : 'form-input', 'placeholder': 'ENTER YOUR NAME*'
            }),
            'email' : forms.EmailInput(attrs={
                'id' : 'contact-email', 'class' : 'form-input', 'placeholder': 'ENTER YOUR EMAIL*'
            }),
            'phone' : forms.TextInput(attrs={
                'id' : 'contact-phone', 'class' : 'form-input', 'placeholder': 'PHONE NUMBER'
            }),
            'message' : forms.Textarea(attrs={
                'id' : 'contact-message', 'class' : 'form-input', 'placeholder' : 'YOUR MESSAGE*', 'rows' : 5, 'columns' : 40
            })
        }
        