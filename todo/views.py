from django.shortcuts import render, HttpResponse
from .models import item

# Create your views here.

"""Gets items data from database

Creates the item variable by assigning it the item class imported from
models.py and the Django QuerySet method .objects.all(), which retrieves all
instances of the item model from the database. The query set is then passed to
the context dictionary as the value in the key value pair 'items':item and
finally the dictionary is made available to the html template by adding it to
the return render function.
"""

def get_todo_list(request):
    # Creates item variable with .objects.all()
    items = item.objects.all()
    # Creates dictionary using items variable
    context = {
        'items':items
    }
    # Makes context dictionary available to html template
    return render(request, "todo/todo_list.html", context)