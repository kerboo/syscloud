#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://admin:123456@192.168.199.111/kerboo'
db=SQLAlchemy(app)

from auth import views
from auth import models
from auth import forms
