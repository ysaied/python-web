from flask import Flask,redirect,render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3ce935361404fc33e9323360021249c4'

#Below is basic Flask decorator with text about
#@app.route('/')
def hello():
    return "<h1>Hello World!<h1>"

# Below return HTML document from Template directory. 
# That need HTML render module
@app.route('/')
def hello():
    return render_template('home.html')

# Below will push (post) data from database to server side, server HTML will render the data
# and present it to on the HTML .. That is because Flask.render is able to read that data and process
# Jinja functions
# The HTML will render variable named "family", that came from python directory db_01
@app.route('/family')
def family():
    return render_template('family.html', family=db_01, title="Family")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('register.html', title="Login", form=form)

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

# Define database using python list

db_01 = [
   {
       "fname" : "yasser",
       "lname" : "saied",
       "age" : "40",
       "gender" : "male",
   },
   {
        "fname" : "eman",
       "lname" : "alkholy",
       "age" : "38",
       "gender" : "fmale",
   }
]

#app.debug = True
app.run(host= "0.0.0.0", debug=True)
#app.run(debug = True)
