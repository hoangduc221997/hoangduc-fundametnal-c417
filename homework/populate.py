from models.customer import Customer
import mlab
from random import randint, choice
from faker import Faker
from cFake import *

mlab.connect()
fake=Faker()

for i in range(50):
    g = randint(0,1)
    print("saving data...",i+1,".....")
    if g == 0:
        i = female_image()
    if g == 1 :
        i = male_image()
    data = Customer(name = fake.name(),
                    gender = g,
                    email=fake.email(),
                    yob = randint(1900,2000)
                    phone=fake.phone_number(),
                    address=fake.address(),
                    company=fake.company(),
                    contacted=choice([True,False]),
                    description = description(),
                    measurements = measurements(),
                    image = i)

    data.save()
