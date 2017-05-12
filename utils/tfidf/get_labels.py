#!/usr/bin/env python
# encoding: utf-8


#数据库读取收藏的文章
#对所有文章提取关键字
#提取关键字

from orm import Collect,Resource
from init import session,mongodb,app,jsonify
#uid=session['user']['user_id']

@app.route('/labels')
def get_labels():
    if session.has_key('user'):
        user=session['user']
        uid=user['user_id']
    else:
        return "<h1>Hello World"
    try:
    	from bs4 import BeautifulSoup
    	cs=Collect.query.filter_by(user_id=uid)

    	all=""
    	all_tags=list()
    	for tmp in cs:
        	rid=tmp.resource_index
        	resource=Resource.query.filter_by(resource_id=rid).first()
        	oid=resource.objectid
        	from bson import ObjectId
        	data=mongodb.data.find_one({'tid': 3,"_id":ObjectId(oid)})
        	txt = data['content']['body']
        	soup = BeautifulSoup(txt)
        	title = soup.find("h2", class_="question-title").text
        	text = ""
        	tempdiv = soup.find("div", class_="content")
        	p = tempdiv.find_all("p")
        	for i in p:
                	text = text + (i.text).encode('utf-8')

        	import jieba.analyse
        	#jieba.analyse.set_idf_path("/Users/sen-ele/PycharmProjects/recommendation/utils/tfidf/Cobuild.txt")
        	#jieba.analyse.set_idf_path("/home/tristan/postgradute/mya/recommendation/utils/tfidf/Cobuild.txt")
        	topK=2
        	tags = jieba.analyse.extract_tags(text, topK=topK)
        	#print type(tags)
        	#print tags
        	all_tags.extend(tags)
    		print ','.join(all_tags)
    except Exception,e:
	print e
    	return jsonify(all_tags)
