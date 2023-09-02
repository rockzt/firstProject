# Create your views here.
# Import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Importing models to use DB data
from bootcamp.models import Koder

# Create your views here.
# Views are functions
# view recieve client's request


def get_koder(request, id):
    """koders = [
        {"id": 1 ,"name": "rock", "generation": "2021", "bootmcap": "python back end", "is_active": True, },
        {"id": 2 ,"name": "david", "generation": "2023", "bootmcap": "front end", "is_active": True, },
        {"id": 3 ,"name": "ashley", "generation": "2019", "bootmcap": "swift", "is_active": False, }
    ]
    find_koder = [koder for koder in koders if koder["id"] == id]

    :param request: 
    :param id: 

    """
    try:
        find_koder = Koder.objects.get(pk=id)
        context = {
            "bootcamp": {"name": "Python", "module": "Django"},
            "koders": [find_koder],
        }
    except Koder.DoesNotExist:
        find_koder = ""
        context = {
            "bootcamp": {"name": "Python", "module": "Django"},
            "koders": find_koder,
        }

    # Calling template
    template = loader.get_template("templates/list_koders.html")

    return HttpResponse(template.render(context, request))


def list_koder(request):
    """

    :param request: 

    """
    # Response
    koders = Koder.objects.all()
    print(koders)
    context = {"bootcamp": {"name": "Python", "module": "Django"}, "koders": koders}
    # Calling template
    template = loader.get_template("templates/list_koders.html")

    return HttpResponse(template.render(context, request))


def list_mentors(request):
    """

    :param request: 

    """
    mentors = [
        {"name": "Benjamin", "last_name": "Aguilar", "is_active": True},
        {"name": "Alfredo", "last_name": "Altamirano", "is_active": True},
        {"name": "Charles", "last_name": "Lopez", "is_active": False},
    ]

    context = {"mentors": mentors}
    # Calling template
    template = loader.get_template("templates/list_mentors.html")

    return HttpResponse(template.render(context, request))
