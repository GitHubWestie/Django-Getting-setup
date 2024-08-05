# imports the django forms library
from django import forms
# imports my item model from models.py
from .models import item


class item_form(forms.ModelForm):
    """ Create Django form using django library

    Defines a new form class which inherits form.ModelForm from Django forms.
    ModelForm is a built-in helper class that creates a form from a Django 
    model. The Meta class is used to specify options for the ModelForm. The
    meta class is a standard convention in Django. model = item is the
    imported model and fields = ['name', 'done'] defines which fields to use
    from that model.
    """
    class Meta:
        model = item
        fields = ['name', 'done']