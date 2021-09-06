"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.

If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

number_of_items = int(input('How many items are there? '))
total_price = float(0)
# collect prices for each item
for i in range(1, number_of_items+1):
    item_price = float(input('Price of item: '))
    total_price += item_price
if total_price >= 100:
    total_price = total_price * .9
print('Total price of',number_of_items,f'items is: {total_price:.2f}')
