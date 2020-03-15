from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

users = {
   "yasser" : "yasser123",
   "yaseen" : "yaseen123",
   "ahmed" : 'ahmed123',
   "eman" : "eman123"
}

@app.route('/welcome')
def welcome():
   return render_template ('welcome.html', username = "Yasser")

@app.route('/unauthorized')
def unauthorized():
   return render_template ('unauthorized.html')

def check_login(username, password):
   if users.get(username) == password:
      return redirect(url_for('welcome'))
   else:
      return redirect(url_for('unauthorized'))

@app.route('/', methods=['POST', 'GET'])
def login():
   if request.method == "POST":
      uname = request.form.get('username')
      pword = request.form.get('password')
      return request.form.getlist('username[]')
#      return check_login(uname, pword)
#      return redirect(url_for('test', uname=uname))
#      return test(uname)
#      return request.form
   return render_template('access.html')

app.run(host= "172.16.67.12", debug = True)