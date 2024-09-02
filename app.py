from flask import Flask

app = Flask(__name__)

from flask import request, redirect

from flask import render_template

@app.route("/mypage/me")
def mypageme():
    return render_template("child.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def mypagecontact():
    if request.method == 'GET':
        return render_template("child2.html")
    elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/me")