from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load data
try:
    sales_data = pd.read_csv('sales_data.csv')
    inventory_data = pd.read_csv('inventory_data.csv')
except FileNotFoundError:
    print("Error: Data files not found.")
    exit()

def which_sweet_sells_more_in_month(month, year):
    monthly_sales = sales_data[(sales_data['month'] == month) & (sales_data['year'] == year)]
    if monthly_sales.empty:
        return None, None  # Handle empty data
    
    sweet_sales = monthly_sales.groupby('sweet_id')['quantity_sold'].sum()
    top_sweet = int(sweet_sales.idxmax())  # Convert to native Python int
    top_sweet_sales = int(sweet_sales[top_sweet])  # Convert to native Python int
    print(f"Top sweet: {top_sweet}, Top sweet sales: {top_sweet_sales}")  # Debugging info
    return top_sweet, top_sweet_sales

def highest_revenue_month(year):
    sales_data['revenue'] = sales_data['quantity_sold'] * sales_data['price_per_unit']
    monthly_revenue = sales_data[sales_data['year'] == year].groupby('month')['revenue'].sum()
    if monthly_revenue.empty:
        return None, None  # Handle empty data
    
    top_month = int(monthly_revenue.idxmax())  # Convert to native Python int
    top_revenue = float(monthly_revenue[top_month])  # Convert to native Python float
    print(f"Top month: {top_month}, Top revenue: {top_revenue}")  # Debugging info
    return top_month, top_revenue

def yearly_sales_comparison():
    yearly_sales = sales_data.groupby('year')['quantity_sold'].sum()
    if yearly_sales.empty:
        return {}  # Handle empty data
    
    yearly_sales_dict = yearly_sales.astype(int).to_dict()  # Convert to native Python int
    print(f"Yearly sales: {yearly_sales_dict}")  # Debugging info
    return yearly_sales_dict

def most_wasted_sweet():
    inventory_data['unsold'] = inventory_data['initial_stock'] - inventory_data['sold']
    if inventory_data['unsold'].empty:
        return None, None  # Handle empty data
    
    most_wasted = int(inventory_data['unsold'].idxmax())  # Convert to native Python int
    wasted_quantity = int(inventory_data['unsold'][most_wasted])  # Convert to native Python int
    print(f"Most wasted sweet: {most_wasted}, Wasted quantity: {wasted_quantity}")  # Debugging info
    return most_wasted, wasted_quantity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top_sweet', methods=['GET'])
def top_sweet():
    try:
        month = int(request.args.get('month'))
        year = int(request.args.get('year'))
        top_sweet, top_sweet_sales = which_sweet_sells_more_in_month(month, year)
        if top_sweet is None:
            return jsonify({'error': 'No data found for the given month and year'}), 404
        return jsonify({'top_sweet': top_sweet, 'top_sweet_sales': top_sweet_sales})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/top_revenue_month', methods=['GET'])
def top_revenue_month():
    try:
        year = int(request.args.get('year'))
        top_month, top_revenue = highest_revenue_month(year)
        if top_month is None:
            return jsonify({'error': 'No data found for the given year'}), 404
        return jsonify({'top_month': top_month, 'top_revenue': top_revenue})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/yearly_sales', methods=['GET'])
def yearly_sales():
    try:
        yearly_sales = yearly_sales_comparison()
        if not yearly_sales:
            return jsonify({'error': 'No yearly sales data available'}), 404
        return jsonify(yearly_sales)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/most_wasted', methods=['GET'])
def most_wasted():
    try:
        most_wasted, wasted_quantity = most_wasted_sweet()
        if most_wasted is None:
            return jsonify({'error': 'No data available for most wasted sweet'}), 404
        return jsonify({'most_wasted': most_wasted, 'wasted_quantity': wasted_quantity})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
