from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/user/<username>')
def index(username):
    user = {
        'D':{
            'name':'Mr D',
            'age':100,
            'gender':'male'
        },
        'A':{'name':'Mr.A',
             'age':200,
             'gender':'Gay'
             },
        'B':{'name':'Ms B',
             'age':12,
             'gender':'Lesbian',
             },
        'C':{'name':'Ms C',
             'age':13,
             'gender':'Male'}
    }

    if username in user.keys():
        post = user[username]
        return render_template('exhigh.html',post=post)
    else:
        return 'User not found'

if __name__ == '__main__':
    app.run(debug=True)
