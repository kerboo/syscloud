#!/usr/bin/env python
# -*- coding=utf-8 -*-
from auth import app
from flask import render_template,url_for,redirect,session,request
from .forms import LoginForm
from auth.models import User

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def index():
    bdf = LoginForm(request.form)
    if request.method == 'POST' and bdf.validate():
        u_name = User.query.filter_by(username=bdf.username.data).first()
        u_pwd = User.query.filter_by(password=bdf.password.data).first()
        if  u_name is not None  and  u_pwd is not None:
            return redirect(url_for("logined"))
        else:
            message="Login Failed"
            return render_template("login.html", message=message)
    return render_template("login.html",form=bdf)


@app.route("/dirsed")
def logined():
    return render_template("Dirsed.html")


#@app.route("/adduser")
#def add_user():
