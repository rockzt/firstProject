from django.db import models

# Create your models here.

# Koder`s Data
# id -> SERIAL autoincrement
# first_name -> string
# last_name -> string
# generation -> string
# email -> string
# phone -> string
# status -> string (activo, dado de baja)
# address -> string
# size -> (s, m, l)
# created_at -> date
# updated_at -> date
# birthdate  -> date

# las clases(modelos) van capitalizadas -> Koder
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiead de la clase(modelo) representa un atributo en la tabla

class Koder(models.Model):
    """Koder Model."""
    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("finished", "Finished")
    ]

    SIZES = [
        ("s", "Small"),
        ("m", "Medium"),
        ("l", "Large")
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    generation = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8, choices=STATUSES, default="activo")
    address = models.CharField(max_length=255)
    size = models.CharField(max_length=1, choices=SIZES, default="s")
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    # Function that represents a Koder
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}, Email -> {self.email}"

'''
from bootcamp.models import Koder
import datetime
Koder.objects.create(first_name='rito', last_name='yagami', generation='2023',email='rito@gmail.com',phone='3245678',address='takome #130 tokyo, JPN', birthdate=datetime.datetime(2000,09,04))
select_koders_query = Koder.objects.all()
# Accesing List Elements
print(select_koders_query[0].email)  
print(select_koders_query[0].name)
print(select_koders_query[1].email)
print(select_koders_query[1].name)
# Can also access to elements not declared on __str__()
print(select_koders_query[1].created_at)
print(select_koders_query[0].birthdate)

# Selecting specific record from DB, PK to auto-created value or can use another field that is unique, return 1 value
Koder.objects.get(pk=2)
Koder.objects.get(email="rock@gmail.com")

# Acts like where clause, returns a list
Koder.objects.filter(first_name="rock")
Koder.objects.filter(first_name="rock")[0].last_name   #Accesing specific value

# Exclude records
Koder.objects.exclude(first_name="rito")
'''