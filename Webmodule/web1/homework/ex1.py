from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/bmi/<float:w>/<float:h>)')

def index(w,h):
    h/=100
    bmi=(w/(h*h))
    if bmi <16:
        result='Severe underweight'
    elif bmi <18.5:
        result='Underweight'
    elif bmi<25:
        result='Normal'
    elif bmi<30:
        result='Overweigt'
    else:
        result='Obese'
    return"Your Fucking BMI:{0}. You are {1} noob".format(bmi,result)
if __name__=="__main__":
    app.run(port=2000,debug=True)
