from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/test')
def test():
    Test = { "fname" : "Yasser", "lname" : "Saied" }
    return Test


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

app.run(host= "172.16.67.12")
