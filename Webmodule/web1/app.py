from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():

    posts = [{
        "title":"Tho con kettt",
        "content":"Ahihi",
        "author":"Dzzz",
        "gender":1},
        {  "title":"Tho con kuu",
        "content":"Lay chua ",
        "author":"zzz",
        "gender":0},
        {
        "title":"Sam Son",
        "content":"OG KUSH",
        "author":"Dzz",
        "gender":1}
        ]

    title = "tho con kett"
    content = "Ahihi"
    author = "Dzz"
    # return render_template("index.html",post_title=title,post_content=content,post_author=author)
    return  render_template("index.html",posts=posts)
@app.route('/choi em di')
def sayhi():
    return("Cang qua")

@app.route('/sayhello/<name>/<age>')
def sayoye(name,age):
    return "Hi {0},you are {1} year olds".format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def calc(a,b):

    return str(a + b)
    #return "String"
    # return ("{0}".format(int(a)+int(b)))
    # return str(int(a) + int(b))
if __name__ == '__main__':
  app.run(port=4200,debug=True)
