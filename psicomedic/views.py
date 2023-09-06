from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # importing to use template loader
from psicomedic.models import Psychologist, Patient, Appointment


# Create your views here.


def welcome(request):
    # Response
    html = """
    <html>
    <body>
       <div>
            <h1 style="text-align:center;">Welcome!</h><b><hr></b>
        </div>
        <p style="text-align:center">
        Welcome to Psicomedic
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)


def customgreet(request, name):
    # Response
    context =  {"name":name}  # Used to pass values to templates
    template = loader.get_template("templates/base.html")
    return HttpResponse(template.render(context, request))



def list_psychologists(request):
    list_psychologists = Psychologist.objects.all()
    context = {
        "psychologists": list_psychologists
    }
    # Calling template
    template = loader.get_template("templates/psychologist_psicomedic.html")
    return HttpResponse(template.render(context, request))


def get_psychologist(request, id):
    try:
        find_psychologist =Psychologist.objects.get(pk=id)
        context = {
            "psychologists": [find_psychologist]
        }
    except Psychologist.DoesNotExist:
        find_psychologist = ""
        context = {
            "psychologists": find_psychologist
        }

    # Calling template
    template = loader.get_template("templates/psychologist_psicomedic.html")
    return HttpResponse(template.render(context, request))


def list_patients(request):
    list_patient = Patient.objects.all()
    context = {
        "patients": list_patient
    }
    # Calling template
    template = loader.get_template("templates/patient_psicomedic.html")
    return HttpResponse(template.render(context, request))


def get_patient(request, id):
    try:
        find_patient =Patient.objects.get(pk=id)
        context = {
            "patients": [find_patient]
        }
    except Patient.DoesNotExist:
        find_patient = ""
        context = {
            "patients": find_patient
        }

    # Calling template
    template = loader.get_template("templates/patient_psicomedic.html")
    return HttpResponse(template.render(context, request))


def list_appointments(request):
    list_appointment = Appointment.objects.all()
    context = {
        "appointments": list_appointment
    }
    # Calling template
    template = loader.get_template("templates/appointment_psicomedic.html")
    return HttpResponse(template.render(context, request))


def get_appointment(request, id):
    try:
        find_appointment =Appointment.objects.get(pk=id)
        context = {
            "appointments": [find_appointment]
        }
    except Appointment.DoesNotExist:
        find_appointment = ""
        context = {
            "appointments": find_appointment
        }

    # Calling template
    template = loader.get_template("templates/appointment_psicomedic.html")
    return HttpResponse(template.render(context, request))

