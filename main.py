# data types in Python
from pyscript import display

restaurant_name = 'Yum-nilla' # script
business_hours = '9 : 00 am - 6 : 00 pm' # script
year_established = 2025 # integer
owner_fname = 'Ivy' # script
owner_lname = 'Zosa' # script
popular_item_price = 59.0 # floating-point

product_flavor = 'Vanilla' # script
product_names = ['Ice cream', 'Cake', 'Milkshake', 'Yogurt', 'Pudding'] # list
product_prices = 59.0, 70.0, 87.0, 105.0, 187.0 # tuple
common_allergens = 'Milk, Eggs, Nuts' # script
tax_rate = 0.09 # floating-point
has_delivery = True

# Total types: ( 1 ) script ( 2 ) integer ( 3 ) floating-point ( 4 ) list ( 5 ) tuple ( 6 ) boolean

# Header --- Shop title, owners name, year established
display(f'Welcome to {restaurant_name} !', target='shoptitle')
display(f'Owner : {owner_fname} {owner_lname}', target='ownersname')
display(f'Since {year_established}', target='yearestablished')


# Table content --- Product names and prices
display(f'tax rate : {tax_rate} ₱', target='taxrate')

display(f'{product_flavor} {product_names[0]}', target='Ice_cream_product')
display(f'{product_prices[1]} ₱', target='Ice_cream_price')

display(f'{product_flavor} {product_names[1]}', target='Cake_product')
display(f'{product_prices[4]} ₱', target='Cake_price')

display(f'{product_flavor} {product_names[2]}', target='Milkshake_product')
display(f'{popular_item_price} ₱', target='Milkshake_price')

display(f'{product_flavor} {product_names[3]}', target='Yogurt_product')
display(f'{product_prices[2]} ₱', target='Yogurt_price')

display(f'{product_flavor} {product_names[4]}', target='Pudding_product')
display(f'{product_prices[3]} ₱', target='Pudding_price')

if has_delivery:
    display("Delivery available !", target="deliverystatus");
else:
    display("Sorry, delivery Unavailable !", target="deliverystatus");

# Common Allergens

display(f'! ! Be careful, our products contain : {common_allergens}.', target='commonallergens')

# Business hours
display(f'{business_hours}', target='businesshours')