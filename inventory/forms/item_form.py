from inventory.models import Item, Location
from django.forms import ModelForm, DateInput


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['id','item_type', 'name', 'photo', 'location','sublocation', 'purchase_date', 'stock', 'description']
        widgets = {'purchase_date': DateInput(attrs={'type':'date'})}