from flask import Flask,render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    me ={"name":"Hoang Duc",
           "work":"student",
           "school":"FTU",
           "hobies":"smoke wee",
           "dog":"RUC"
            }
    return render_template("index.html",me=me)

@app.route('/school')
def school():
    return redirect("http://techkids.vn",code=305)


if __name__=='__main__':
    app.run(port=5000,debug=True)
