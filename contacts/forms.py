from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'email', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "To'liq ism sharifingiz"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "+998 XX XXX-XX-XX"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "email@example.com"}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Murojaatingiz mavzusi"}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': "Xabaringizni yozing..."}),
        }
        labels = {
            'full_name': "F.I.Sh.",
            'phone': "Telefon raqam",
            'email': "Elektron pochta",
            'subject': "Mavzu",
            'message': "Xabar",
        }
