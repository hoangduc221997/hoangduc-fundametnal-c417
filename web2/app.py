#fapp
from flask import Flask, render_template
import mlab
from mongoengine import *
from models.service import Service
# from mongoengine import *
app = Flask(__name__)
#inherit
mlab.connect()

#design database
# create collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()
#
# service = Service(name ="Khong Minh",
#                   yob=350,
#                   gender =1,
#                   height=178,
#                   phone = "01211242340",
#                   address="Thuc quoc",
#                   status = False)
#
# service.save()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender = g,yob__lte=2000,address__contains="quoc")
    return render_template('search.html',all_service=all_service)



if __name__ == '__main__':
  app.run( debug=True)
