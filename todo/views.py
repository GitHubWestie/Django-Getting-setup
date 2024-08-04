from django.shortcuts import render, redirect
from .models import item

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
    """ Gets data submitted from form

    If request method is GET (i.e if page is being loaded) then the return
    render at the end of the function will run. If the form is submitted then
    the if statement will be entered as this will be a POST request. The name
    and done variables are then assigned values from the form based on the 
    name attribute from the form field. These variables are then assigned to
    the name and done fields in the model and sent to the database using the
    objects manager built into Django
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        item.objects.create(name=name, done=done)

        return redirect(get_todo_list)
    return render(request, "todo/add_item.html")