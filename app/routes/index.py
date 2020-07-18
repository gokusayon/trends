# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:10:53 2020

@author: vedvp
"""

from flask import Blueprint, jsonify, request
from wrapper import index, AsyncUpdateRealTimeTask, fetch_expires, fetch_strike_prices, paginate
from datetime import  datetime

index_route = Blueprint('index', __name__, url_prefix='/index')

# index = Index()
    
@index_route.route('/', methods = ['POST'])
def post():
    data = request.get_json() 
    return index.post(data)
    
@index_route.route('/', methods = ['GET'])
def get():
    data = request.get_json() 
    return index.get()
    
@index_route.route('/', methods = ['PUT'])
def put():
    data = request.get_json()
    async_task = AsyncUpdateRealTimeTask(task_details=data)
    async_task.start()
    return "Success"
    
@index_route.route('/', methods = ['DELETE'])
def delete():
    return index.delete()
    
@index_route.route('/freeze', methods = ['POST'])
def post_freeze():
    data = request.get_json()
    index.post_freeze(data)
    return get_freeze()
    
@index_route.route('/freeze', methods = ['GET'])
def get_freeze():
    return index.get_freeze()
    
@index_route.route('/name', methods = ['GET'])
def name():    
    return index.name()

@index_route.route('/expiry', methods = ['GET'])
def fetch_expiry(): 
    data = request.get_json()    
    if 'instrument' in data:
        return jsonify(fetch_expires(data))
    else:
        return []    
    
@index_route.route('/strike', methods = ['GET'])
def fetch_sp(): 
    data = request.get_json()    
    if 'instrument' in data:
        return jsonify(fetch_strike_prices(data))
    else:
        return []
    
@index_route.route('/history/<int:page>/<int:size>', methods = ['GET'])
def history(page, size):
    df = paginate(page, size)
    return jsonify(df)