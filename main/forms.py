from django import forms
from .models import Registration, Contact, Career



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["from_user", "from_email", "phone_number"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "number", "message" ]


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ["teach_name", "teach_email", "teach_message"]
