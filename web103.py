from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/welcome')
def welcome():
   return render_template ('welcome.html')

@app.route('/unauthorized')
def unauthorized():
   return render_template ('unauthorized.html')

def check_login(username, password):
   if (username == "ysaied"  and password ==  "yasser123"):
      return redirect ('welcome.html')
   else:
      return redirect ('unauthorized.html')


@app.route('/', methods=['POST', 'GET'])
def login():
   if request.method == "POST":
      uname = request.form.get('username')
      pword = request.form.get('password')
      return check_login(uname, pword)
#      return check_login(uname, pword)
#      return redirect(url_for('test', uname=uname))
#      return test(uname)
#      return request.form
   return render_template('access.html')

app.run(host= "172.16.67.12")