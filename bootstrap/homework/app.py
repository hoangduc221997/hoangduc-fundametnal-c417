from flask import *
import mlab
from models.customer import Customer
from jinja2 import Template

app = Flask(__name__)
mlab.connect()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete/<customer_id>')
def delete(customer_id):
    customer_del = Customer.objects.with_id(customer_id)
    if customer_del is not None:
        customer_del.delete()
    return redirect(url_for('admin'))

@app.route('/customer')
def search():
    all_customer=Customer.objects()
    return render_template('search.html',all_customer=all_customer)

@app.route('/detail,<customer_id>')
def detail(customer_id):
    customer_id = Customer.objects.with_id(customer_id)
    return render_template('detail.html',customer_id=customer_id)

@app.route('/customer/<g>')
def customer(g):
    all_customer=Customer.objects(contacted=False,gender = g)
    return render_template('search.html',all_customer=all_customer)


@app.route('/admin')
def admin():
    all_customer  = Customer.objects()
    return render_template('admin.html',all_customer = all_customer)



@app.route('/delete_all')
def delete_all():
    all_customer = Customer.objects()
    for customer in all_customer:
        customer.delete()
    return render_template ('search.html')

@app.route('/new',methods =['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        gender = form['gender']
        phone = form['phone']
        customer = Customer(name = name, gender = gender,phone = phone)
        customer.save()
        return redirect(url_for('admin'))

@app.route('/update/<customer_id>',methods=['GET','POST'])
def update(customer_id):
    if request.method == 'GET':
        customer = Customer.objects.with_id(customer_id)
        return render_template ('update.html',customer = customer)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        gender = form['gender']

        phone = form['phone']
        address = form['address']
        contacted = form['contacted']
        description = form['description']
        measurements = form['measurements']

        customer = Customer.objects.with_id(customer_id)
        customer.update(set__name =name,
                        set__gender = gender,
                        set__phone = phone,
                        set__address = address,
                        set__contacted = bool(contacted),
                        set__description = description,
                        set__measurements= measurements,
                    )
        customer.reload()
        return redirect(url_for('admin'))





if __name__ == '__main__':
  app.run(port=8000,debug=True)
