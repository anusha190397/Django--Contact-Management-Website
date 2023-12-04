from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'note']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Your validation logic for name uniqueness goes here
        if not self.instance.pk and Contact.objects.filter(name=name).exists():
            raise forms.ValidationError("A contact with this name already exists.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Using Django's built-in email validation
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Please enter a valid email address.")
        
        # Additional validation for email uniqueness
        if not self.instance.pk and Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("A contact with this email already exists.")
        return email

    def clean_created_time(self):
        created_time = self.cleaned_data.get('created_time')
        # Your validation logic for created_time goes here
        return created_time
