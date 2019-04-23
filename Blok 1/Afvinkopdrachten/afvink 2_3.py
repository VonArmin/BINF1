item1 = float(input('what is the price of item 1? :'))
item2 = float(input('what is the price of item 2? :'))
item3 = float(input('what is the price of item 3? :'))
item4 = float(input('what is the price of item 4? :'))
item5 = float(input('what is the price of item 5? :'))
subtotal = item1 + item2 + item3 + item4 + item5
total = subtotal * 1.07
tax = total - subtotal
print('the subtotal price is', subtotal)
print('the total price included with tax is', round(total,1))
print('the amount of tax is', round(tax,1))
