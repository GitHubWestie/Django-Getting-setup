from django.shortcuts import render, redirect
from .models import item
from .forms import item_form

# Create your views here.


def get_todo_list(request):
    """Gets items data from database

    Creates the item variable by assigning it the item class imported from
    models.py and the Django QuerySet method .objects.all(), which retrieves all
    instances of the item model from the database. The query set is then passed to
    the context dictionary as the value in the key value pair 'items':item and
    finally the dictionary is made available to the html template by adding it to
    the return render function.
    """

    # Creates item variable with .objects.all()
    items = item.objects.all()
    # Creates dictionary using items variable
    context = {
        'items':items
    }
    # Makes context dictionary available to html template
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == 'POST':
        form = item_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    form = item_form()
    context = {
        'form': form
    }
    return render(request, "todo/add_item.html", context)