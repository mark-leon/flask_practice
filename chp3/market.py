from chp3 import app
from flask import render_template


@app.route("/")
@app.route('/home')
def home_page():
 return render_template('home.html')


@app.route('/market')
def market_page():
 items = [{'id':1,'name':'Phone','barcode':'2907489374','price':500}, 
          {'id':2,'name':'Laptop','barcode':'1247489374','price':500},
          {'id':3,'name':'Keyboard','barcode':'8997489374','price':500}]
 return render_template('market.html',items=items)