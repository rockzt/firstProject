from django.urls import path
# Importing custom view
from .views import get_koder, list_koder, list_mentors

# urls
urlpatterns = [
    # Custom URLs
    path("koder/<int:id>/", get_koder),
    path("koders/", list_koder),
    path("mentors/", list_mentors)
]
