import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_file():
    products = []

    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql_file():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()

    products = [dict(row) for row in rows]

    conn.close()

    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            product_list = read_json_file()
        elif source == 'csv':
            product_list = read_csv_file()
        elif source == 'sql':
            product_list = read_sql_file()
        else:
            return render_template(
                'product_display.html',
                products=[],
                error='Wrong source'
            )

    except (OSError, json.JSONDecodeError, sqlite3.Error):
        return render_template(
            'product_display.html',
            products=[],
            error='Error reading data'
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

        product_list = [
            product for product in product_list
            if product['id'] == product_id
        ]

        if not product_list:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=product_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)