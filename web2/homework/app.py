from flask import Flask, render_template
import mlab
from models.customer import Customer
from jinja2 import Template

app = Flask(__name__)
mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def search():
    all_customer=Customer.objects()
    return render_template('search.html',all_customer=all_customer)

@app.route('/customer/<g>')
def customer(g):
    all_customer=Customer.objects[:10](contacted=False,gender = g)
    return render_template('search.html',all_customer=all_customer)



if __name__ == '__main__':
  app.run(debug=True)
