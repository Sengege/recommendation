#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: index.py
@time: 17/4/17 PM8:40
"""
import json

from WebUI.ui import render_template
from APIserver.init import app,session


@app.route('/test/home')
def home():
    moives=get_movie().get_data()
    books=get_book().get_data()
    daily=get_zhdaily().get_data()
    content=dict()
    content['movies']=json.loads(moives)
    content['books']=json.loads(books)
    content['daily']=json.loads(daily)
    return render_template("home.html",content=content)

@app.route('/')
def index():
    uid=session.has_key('user')
    if uid:
        return render_template("index.html")
    else:
        return render_template("auth.html")