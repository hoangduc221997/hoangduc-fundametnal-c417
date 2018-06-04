from mongoengine import *


class Customer(Document):
    name = StringField()
    gender = IntField()
    email=StringField()
    phone = StringField()
    job=StringField()
    company=StringField()
    address=StringField()
    contacted=BooleanField()
    description = StringField()
    measurements=ListField()
    image = StringField()
