from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dataclasses import dataclass
import requests
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)

@dataclass
class Shop(db.Model):
    id: int
    shop_name: str
    shop_address: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop_name = db.Column(db.String(200))
    shop_address = db.Column(db.String(200))

@dataclass
class Order(db.Model):
    id: int
    shop: str
    address: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop = db.Column(db.Integer)
    address = db.Column(db.String(200))

@app.route('/api/shop')
def index():
    return jsonify(Shop.query.all())

@app.route('/api/order/<int:id>/deliver_finish', methods=['POST'])
def deliver_finish(id):
    publish('order_deliverfinished', id)

    return jsonify({
        'message':'success'
    })

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')