# Created by: Gavin Zhou
# Created on: Oct 12 2017
# Created for: ICS3U

import ui
tax = 0.13

def calculate_touch_up_inside(sender):
    
    pizza_size = view['pizza_size_textfield'].text
    topping = view['amount_topping_textfield'].text
    
    
    
    if pizza_size == 'large':
        pizza_size_cost = 6
    elif pizza_size == 'extra large':
        pizza_size_cost = 10
    
    if topping == '1':
        pizza_topping_cost = 1.00
    elif topping == '2':
        pizza_topping_cost = 1.75
    elif topping == '3':
        pizza_topping_cost = 2.50
    elif topping == '4':
        pizza_topping_cost = 3.25
    else:
        view['sorry_textfield'].text ='follow what i put topping only can be 1-4 thanks'
    
    sub_tatal = pizza_size_cost + pizza_topping_cost
    price = sub_tatal * tax + sub_tatal
    
    view['price_textfield'].text = 'show price: ' + str(price)
    
    
view = ui.load_view()
view.present('full screen')
