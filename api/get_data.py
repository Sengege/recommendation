#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: get_data
@time: 25/4/17 PM10:56
"""
from init import app,db_mongo,jsonify
import random
@app.route('/get/zhihudaily')
def get_zhdaily():
    content=list()
    for i in range(10):
        cursor=db_mongo.data.find({"tid":3})
        seed=random.randint(0,cursor.count()-1)
        cursor.skip(seed)
        dl=cursor.next()
        dl['oid']=str(dl.pop('_id'))
        content.append(dl)
        if len(content)>=1:
            break

    return jsonify(content)

@app.route('/get/movie')
def get_movie():
    content=list()
    for i in range(10):
        cursor=db_mongo.data.find({"tid":1})
        seed=random.randint(0,cursor.count()-1)
        cursor.skip(seed)
        dl=cursor.next()
        dl['oid']=str(dl.pop('_id'))
        content.append(dl)
        if len(content)>=3:
            break

    return jsonify(content)

@app.route('/get/book')
def get_book():
    content=list()
    for i in range(10):
        cursor=db_mongo.data.find({"tid":2})
        seed=random.randint(0,cursor.count()-1)
        cursor.skip(seed)
        dl=cursor.next()
        oid=dl.pop('_id')
        dl['oid']=str(oid)
        content.append(dl)
        if len(content)>=1:
            break

    return jsonify(content)