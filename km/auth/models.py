#!/usr/bin/env python
# -*- coding=utf-8 -*-
from auth import db


class User(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(120))
    email  = db.Column(db.String(60))



    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.email = email

