from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

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
   return render_template('access.html')

app.run(host= "172.16.67.12")