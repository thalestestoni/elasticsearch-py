from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

es = Elasticsearch()
app = Flask(__name__)


@app.route('/info')
def info():
    return jsonify(es.info())

@app.route('/products/store', methods=['POST'])
def store():
    response = es.index(
        index = 'products',
        body = request.data
    )
    return response

@app.route('/products/show', methods=['GET'])
def show():
    response = es.get(
        index='products',
        id=request.args.get('id'),
        filter_path=['_id', '_index', '_source']
    )
    return response

@app.route('/products/index', methods=['GET'])
def index():
    response = es.search(
        index='products',
    )
    return response

@app.route('/products/delete', methods=['DELETE'])
def destroy():
    response = es.destroy(
        index='products',
        id=request.args.get('id'),
        filter_path=['_id', '_index', 'result'],
    )
    return response

@app.route('/products/update', methods=['PUT'])
def update():
    response = es.index(
        index='products',
        id=request.args.get('id'),
        body=request.data
    )
    return response
