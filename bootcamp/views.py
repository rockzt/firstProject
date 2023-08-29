from django.shortcuts import render

# Create your views here.
# Import HTTPResponse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# Views are functions
# view recieve client's request
def get_koder(request, id):
    # Response

    koders = [
        {"id":0, "name": "rock", "genration": "2021", "bootmcap": "python back end"},
        {"id":1, "name": "david", "genration": "2023", "bootmcap": "front end"},
        {"id":2, "name": "ashley", "genration": "2019", "bootmcap": "swift"},
    ]

    find_koder = [koder for koder in koders if koder["id"] == id]
    print(find_koder)
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Welcome koder -> {find_koder[0]["name"]}!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Welcome to bootcamp app!
        {find_koder[0]}
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)



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