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
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"