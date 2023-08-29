from django.urls import path
# Importing custom view
from .views import welcome, farewell, greet, customgreet, associate, get_koder, get_koders

# urls

urlpatterns = [
    # Custom URLs
    path("", welcome),
    path("bye/", farewell),
    path("greet/", greet),
    # Receive parameters
    path("custom_greet/<str:name>", customgreet),
    path("associate_type/<str:type>", associate),
    path("koders/<int:id>", get_koder),
    path("koders/", get_koders)
]
