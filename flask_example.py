#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:55:25 2020

@author: deviantpadam
"""

from flask import Flask
from torch2vec.torch2vec import LoadModel

app = Flask(__name__)
model = LoadModel('/home/deviantpadam/weights.npy')

@app.route('/')
def main():
    
    ids, prob = model.similar_docs(124,topk=10,use='torch')
    ids = [str(i) for i in ids]
    ids = "------------".join(ids)
    type(ids)
    
    prob= [str(i) for i in prob]
    prob = "-----------".join(prob)        
    return ids+prob

if '__main__'==__name__:
    app.run()
