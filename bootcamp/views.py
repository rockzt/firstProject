from django.shortcuts import render

# Create your views here.
# Import HTTPResponse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# Views are functions
# view recieve client's request
def get_koder(request, id):


    koders = [
        {"id": 1 ,"name": "rock", "generation": "2021", "bootmcap": "python back end", "is_active": True, },
        {"id": 2 ,"name": "david", "generation": "2023", "bootmcap": "front end", "is_active": True, },
        {"id": 3 ,"name": "ashley", "generation": "2019", "bootmcap": "swift", "is_active": False, }
    ]

    find_koder = [koder for koder in koders if koder["id"] == id]
    context = {
        "bootcamp": {"name": "Python", "module": "Django"},
        "koders": find_koder
    }
    # Calling template
    template = loader.get_template("list_koders.html")

    return HttpResponse(template.render(context, request))



def list_koder(request):
    # Response
    context = {
        "bootcamp": { "name":"Python", "module":"Django" },
        "koders": [
            {"name": "rock", "generation": "2021", "bootmcap": "python back end", "is_active": True,},
            {"name": "david", "generation": "2023", "bootmcap": "front end", "is_active": True,},
            {"name": "ashley", "generation": "2019", "bootmcap": "swift", "is_active": False,}
        ]
    }
    #Calling template
    template = loader.get_template("list_koders.html")


    return HttpResponse(template.render(context, request))