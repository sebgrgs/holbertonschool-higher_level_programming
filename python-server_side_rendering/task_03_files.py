from flask import Flask, render_template, request
import json
import csv

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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_data = read_json_data()
    else:
        products_data = read_csv_data()

    if product_id:
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
                error="Invalid product ID")

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
