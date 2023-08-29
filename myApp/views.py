from django.shortcuts import render

# Import HTTPResponse
from django.http import HttpResponse

# Create your views here.
# Views are functions
# view recieve client's request
def welcome(request):
    # Response
    html = """
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Welcome!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Welcome to myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)



def farewell(request):
    # Response
    html = """
        <html>
        <body>
           <div>
                <h1 style="text-align:center;">See you soon!!!</h><b><hr></b>
            </div>
            <p style="text-align:center">
            Leaving myApp  
            </p>
        </body>
        </html>
        """
    return HttpResponse(html)


def greet(request):
    # Response
    html = """
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Hello there koders!!!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Hello from myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)


def customgreet(request, name):
    # Response
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Hello there { name } koder!!!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Hello from myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)


def associate(request, type):
    message = ''
    if type == 'mentor':
        message = "Hello mentor, your classes, there you go!."
    elif type == 'koder':
        message = "Hello koder, welcome to kodemia"
    else:
        message = "Your are not allowed to be here!"
    # Response
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">{ message }</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Hello from myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)


def get_koder(request, id):
    message = ''
    if type == 'mentor':
        message = "Hello mentor, your classes, there you go!."
    elif type == 'koder':
        message = "Hello koder, welcome to kodemia"
    else:
        message = "Your are not allowed to be here!"
    # Response
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">koder id -> { id }</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Hello from myApp  
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)



def get_koders(request):
    # Response
    koders = [
        'rodrigo',
        'nana',
        'rito'
    ]
    html = f"""
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">{ koders }</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Hello from
        </p>
    </body>
    </html>
    """

    return HttpResponse(html)