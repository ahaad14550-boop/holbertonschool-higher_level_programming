#!/usr/bin/python3
"""Flask application displaying product data from JSON, CSV, or SQLite."""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data from items.json."""
    with open('items.json') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


def read_json(filepath):
    """Read and return product data from a JSON file."""
    with open(filepath) as f:
        return json.load(f)


def read_csv(filepath):
    """Read and return product data from a CSV file."""
    products = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(product_id=None):
    """Read and return product data from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if product_id is not None:
        cursor.execute(
            'SELECT * FROM Products WHERE id = ?', (product_id,)
        )
    else:
        cursor.execute('SELECT * FROM Products')

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        }
        for row in rows
    ]


@app.route('/products')
def products():
    """Display product data filtered by source and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

    try:
        if source == 'json':
            data = read_json('products.json')
            if product_id is not None:
                data = [p for p in data if p['id'] == product_id]
        elif source == 'csv':
            data = read_csv('products.csv')
            if product_id is not None:
                data = [p for p in data if p['id'] == product_id]
        else:  # source == 'sql'
            data = read_sql(product_id)
    except sqlite3.Error as error:
        return render_template(
            'product_display.html',
            error=f"Database error: {error}"
        )

    if product_id is not None and not data:
        return render_template(
            'product_display.html', error="Product not found"
        )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)