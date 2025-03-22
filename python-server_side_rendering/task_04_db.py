from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_data():
    """Read product data from JSON file"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_data():
    """Read product data from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


def read_sql_data(product_id=None):
    """Read product data from SQLite database"""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = "SELECT id, name, category, price FROM Products"
        params = ()

        if product_id:
            query += " WHERE id = ?"
            params = (product_id,)

        cursor.execute(query, params)

        for row in cursor.fetchall():
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })

        conn.close()
        return products
    except Exception as e:
        print(f"Error reading from database: {e}")
        return []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        product_id_int = None
        if product_id:
            try:
                product_id_int = int(product_id)
            except ValueError:
                return render_template(
                    'product_display.html', error="Invalid product ID")

        products_data = read_sql_data(product_id_int)

    if product_id and source in ['json', 'csv']:
        try:
            product_id = int(product_id)
            filtered_products = [
                p for p in products_data if p['id'] == product_id
            ]
            if not filtered_products:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
            products_data = filtered_products
        except ValueError:
            return render_template(
                'product_display.html',
                error="Invalid product ID"
            )

    if not products_data and product_id:
        return render_template(
            'product_display.html',
            error="Product not found"
        )

    return render_template(
        'product_display.html',
        products=products_data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
