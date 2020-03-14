from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)




@app.route('/welcome/<uname>')
def test(uname = "test"):
    return  "username %s" % uname

def check_login (username, password):
   if (username == "ysaied"  and password ==  "yasser123"):
      return "Welcom %s" % username
   else:
      return "Wrong Username or Password !!!"

@app.route('/', methods=['post', 'get'])
def login():
   if request.method == "POST":
      uname = request.form.get('username')
      pword = request.form.get('password')
      return check_login(uname, pword)
#      return check_login(uname, pword)
#      return redirect(url_for('test', uname=uname))
#      return test(uname)
#      return request.form
   return render_template('login.html')

app.run(host= "172.16.67.12")
