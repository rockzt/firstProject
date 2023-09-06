from django.db import models

# Create your models here.
# las clases(modelos) van capitalizadas -> Koder
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiead de la clase(modelo) representa un atributo en la tabla
'''
                                Relaciones
La foreign key se pone en la N en las relaciones 1 - N                                
koders - pertenece a una generación (en este caso solo pueden pertenecer a una generación) -> 1 generation - N Koders
Cuand hay N - N, la fk se pone en la más chica
Mentores - pertenece a varias generaciones -> N mentors - N generations
Generaciones - pertenece a un bootcamp  -> 1 bootcamp - N generations
'''


class Psychologist(models.Model):
    """Psychologist model."""
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    birthdate = models.DateTimeField(null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    """Patient model."""
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    birthdate = models.DateTimeField(null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    biography = models.CharField(max_length=5000, null=False)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Appointment(models.Model):
    """Appointment Model."""
    date_app = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, models.PROTECT, related_name="appointments")
    psychologist = models.ForeignKey(Psychologist, models.PROTECT,related_name="appointments")
    created_at = models.DateTimeField(auto_now_add=True)
    # Function that represents a Koder
    def __str__(self):
        return f"Date -> {self.date_app}, Patient -> {self.patient}, Psychologist -> {self.psychologist}"

