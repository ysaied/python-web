from flask import Flask,redirect,render_template
app = Flask(__name__)


#@app.route('/')
def hello():
    return "Hello World!"


@app.route('/test')
def test():
    Test = { "fname" : "Yasser", "lname" : "Saied" }
    return Test


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



@app.route('/google')
def google():
    return redirect("http://www.google.com")


@app.route('/')
def file_read():
   file_output = open("junos-output.txt", "r")
   text_all = file_output.read()
   file_output.close()
   return render_template('index.html', content="Hello")

#app.add_url_rule('/', 'test', test)
#app.add_url_rule('/', 'hello_name', <name>)

#app.debug = True
app.run(host= "172.16.67.12")
#app.run(debug = True)
