cart = [('lenovo', 100), ('lenovo', 40), ('ibm', 100)]

criteria = {
    'brand': 'lenovo',
    'price': 100
}

def get_results(**kwargs):
    results = [(brand, price) for brand,price in cart
               if kwargs.get('brand') == brand and kwargs.get('price') == price]
    return results

print(get_results(**criteria))
