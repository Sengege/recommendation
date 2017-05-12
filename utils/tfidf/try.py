#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: ‘sen-ele‘
@license: Apache Licence 
@file: try
@time: 5/5/17 AM11:07
"""
import sys
sys.path.append('../')
import jieba

import jieba.analyse

file_name = 'air_plane.txt'
topK = 3
content = open(file_name, 'rb').read()

jieba.analyse.set_idf_path("Cobuild.txt")
tags = jieba.analyse.extract_tags(content, topK=topK)


print(",".join(tags))