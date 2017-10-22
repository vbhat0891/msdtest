from django import forms
from .models import Hospital, Bed, Patient


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('hospital_name', 'address', 'phone_no',)


class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = (
            'bed_type',)


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'sex', 'time_of_admission', 'condition', 'age',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
