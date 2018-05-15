from models.customer import Customer
import mlab
from random import randint, choice
from faker import Faker

mlab.connect()
fake=Faker()

for i in range(24):
    print("saving data...",i+1,".....")
    data = Customer(name = fake.name(),
                    gender = randint(0,1),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    address=fake.address(),
                    company=fake.company(),
                    contacted=choice([True,False]))
    data.save()
