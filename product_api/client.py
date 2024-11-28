import requests

BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }
    try:
        response = requests.post(BASE_URL, json=product_data)
        if response.status_code == 201:
            print('Product created:', response.json())
        else:
            try:
                error = response.json()
            except ValueError:
                error = response.text
            print('Failed to create product:', error)
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    add_product('Product 1', 'Description for product 1', 19.99)
    add_product('Product 2', 'Description for product 2', 29.99)
    # Define the `get_products()` function or remove this line
    # get_products()
