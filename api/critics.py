#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: critics
@time: 26/4/17 AM12:08
"""
from init import app,jsonify,mysqldb as db
from orm import Resource,Critics
@app.route('/critics/<uid>/<score>/<tid>/<oid>/<id>')
def like(uid,score,tid,oid,id):
    rs=Resource.query.filter_by(objectid=oid).first()
    if not rs:
        new_item=Resource(objectid=oid,type_id=tid,raw_id=id)
        db.session.add(new_item)
        db.session.commit()
        print "New item"
    else:
        new_critics=Critics(resource_id=rs.resource_id,user_id=uid,critics=score)
        db.session.add(new_critics)
        db.session.commit()
        print "add_critics"
    return jsonify("pass")