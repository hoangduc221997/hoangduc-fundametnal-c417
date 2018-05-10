from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/bmi/<float:w>/<float:h>)')
def bmi(w,h):
    h/=100
    bmi1= w/(h*h)
    return render_template('ex11.html',bmi1=bmi1)
if __name__=='__main__':
    app.run(debug=True)
