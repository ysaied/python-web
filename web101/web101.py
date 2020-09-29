from flask import Flask,redirect,render_template
app = Flask(__name__)

#Below is basic Flask decorator with text about
#@app.route('/')
def hello():
    return "<h1>Hello World!<h1>"

# Below return HTML document from Template directory. 
# That need HTML render module
@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return "<h1>About!<h1>"




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


#@app.route('/')
def file_read():
   file_output = open("junos-output.txt", "r")
   text_all = file_output.read()
   file_output.close()
   return render_template('index.html', content=text_all)

#app.add_url_rule('/', 'test', test)
#app.add_url_rule('/', 'hello_name', <name>)

#app.debug = True
app.run(host= "0.0.0.0", debug=True)
#app.run(debug = True)
