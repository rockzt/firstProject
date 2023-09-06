from django.urls import path
# Importing custom view
from .views import welcome, customgreet, list_psychologists, get_psychologist, list_patients, get_patient, list_appointments, get_appointment

# urls

urlpatterns = [
    # Custom URLs
    path("", welcome),
    path("custom_greet/<str:name>", customgreet),
    path("psychologists/", list_psychologists),
    path("psychologists/<int:id>", get_psychologist),
    path("patients/", list_patients),
    path("patients/<int:id>", get_patient),
    path("appointments/", list_appointments),
    path("appointments/<int:id>", get_appointment),
]
