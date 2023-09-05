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

class Bootcamp(models.Model):
    """Bootcamp model."""
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Generation(models.Model):
    """Generation model."""
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign key
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")

    def __str__(self):
        return f"{self.number} {self.bootcamp.name}"


class Koder(models.Model):
    """Koder Model."""
    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("finished", "Finished")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8, choices=STATUSES, default="activo")
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    #Foreign keys
    # 1 generation - N Koders
    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")


    # Function that represents a Koder
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}, Email -> {self.email}"


class Mentor(models.Model):
    """Mentor model."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign key
    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
        return f"id -> {self.pk} {self.first_name}, Email -> {self.last_name}"



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


# Relationship fields
models.ForeignKey()

        Relaciones
koders - pertenece a una generación (en este caso solo pueden pertenecer a una generación) -> 1 generation - N Koders
Mentores - pertenece a varias generaciones -> N mentors - N generations
Generaciones - pertenece a un bootcamp  -> 1 bootcamp - N generations
Bootcamps
        Creating Records using Models ORM with relations
from bootcamp.models import Bootcamp, Generation, Mentor, Koder

 bootcamp_1 = Bootcamp.objects.create(name="ruby")
 generation_1 = Generation.objects.create(number=1, bootcamp=bootcamp)
 
 Bootcamp.objects.create(name="Go")
 generation_go = Generation.objects.create(number=2, bootcamp_id=2)
 
 generation_js.__dict__
 
 generation
 generation.bootcamp.name
 generation_js.bootcamp.name
 
        Advanced queries Relations
Generation.objects.filter(bootcamp=bootcamp)
bootcamp.generations.all()

        Advanced Relations
mentor = Mentor.objects.create(first_name="rem", last_name="ori", email="rem@gmail.com", phone="55836016")
mentor.generations.add(generation_js)
mentor.generations.all()

generation_py = Generation.objects.get(pk=1)
generation_py.mentors.add(mentor)
generation.mentor.all()

geneartion.mentor.all()
'''