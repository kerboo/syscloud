#!/usr/bin/env python
# -*- coding=utf-8 -*-
from wtforms import Form,StringField,BooleanField,validators,PasswordField,SubmitField,IntegerField
from wtforms.validators import Regexp,EqualTo
from wtforms import ValidationError
from .models import User

class LoginForm(Form):
    username = StringField('username',validators=[validators.DataRequired()])
    password = PasswordField('password',validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me',default=False)
    submit  = SubmitField('submit')



class AddUser(LoginForm):
    email = StringField("email",validators=[validators.Email()])
    phone = IntegerField("phone",validators=[validators.DataRequired],length=11)
    username = StringField('username', validators=[validators.DataRequired(),Regexp('^[a-zA-Z][A-Za-z0-9_.]*$',0,message='Username must have only letters')],length=15)
    password = PasswordField('password', validators=[validators.DataRequired(),EqualTo('password2',message="password must mach")])
    password2 = PasswordField('confirm password',validators.DataRequired())
    submit = SubmitField('submit')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registerd')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')
#
#