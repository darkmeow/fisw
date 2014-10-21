from inventory.models import Loan
from django.forms import ModelForm

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ('client', 'item')