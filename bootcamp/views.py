from django.shortcuts import render

# Create your views here.
# Import HTTPResponse
from django.http import HttpResponse

# Create your views here.
# Views are functions
# view recieve client's request
def get_koder(request, id):
    # Response
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Welcome koder -> { id }!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Welcome to myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)



def list_koder(request):
    # Response
    html = """
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Welcome koders: ...!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Welcome to myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)