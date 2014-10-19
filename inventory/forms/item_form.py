from inventory.models import Item, Location
from django.forms import ModelForm, DateInput


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'purchase_date': DateInput(attrs={'type':'date'})}