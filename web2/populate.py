from models.service import Service
from faker import Faker
import mlab
from random import randint,choice

mlab.connect()
fake = Faker()

# print(fake.address())
for i in range(30):
    print("Saving service",i+1,".....")
    service = Service(name =fake.name(),
                      yob= randint(1990,2001),
                      gender =randint(0,1),
                      height=randint(140,190),
                      phone = fake.phone_number(),
                      address= fake.address(),
                      status = choice([True,False]))

    service.save()
