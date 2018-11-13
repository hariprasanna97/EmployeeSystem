from django import forms
from .models import EmployeeInfo


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        # fields = ["first_name", "last_name", "date_of_birth", "email", "previous_employer"]
        fields = ["first_name", "last_name", "email", "previous_employer"]

    # first_name = forms.CharField(label='First name', max_length=100)
    # last_name = forms.CharField(label='Last name', max_length=100)
    # previous_employer = forms.CharField(label='Previous employer', max_length=100)
    # dob = forms.CharField(label='Date of Birth', max_length=100)
class EmailForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', max_length=1000)
    sender = forms.EmailField(label='Sender Email', max_length=100)
    # cc_myself = form.cleaned_data['cc_myself']
