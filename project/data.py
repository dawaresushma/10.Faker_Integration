import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
import django
django.setup()
from random import *
from faker import Faker
from fapp.models import Employee
fake=Faker()

def phone():
    f=str(randint(6,9))
    for i in range(9):
        f=f+str(randint(6,9))
    return int(f)

def populate(n):
    for i in range(n):
        eid=fake.random_int(min=1,max=100)
        efname=fake.first_name()
        elname=fake.last_name()
        edob=fake.date()
        email=fake.email()
        eaddr=fake.address()
        ephone=phone()
        obj=Employee.objects.get_or_create(eid=eid,
                                           efname=efname,
                                           elname=elname,
                                           edob=edob,
                                           email=email,
                                           eaddr=eaddr,
                                           ephone=ephone)

populate(20)