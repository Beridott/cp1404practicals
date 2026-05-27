number_of_items = int(input("Number of items: "))

total_price = 0
DISCOUNT = 0.1
DISCOUNT_THRESHOLD = 100

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > DISCOUNT_THRESHOLD:
    total_price *=  (1 - DISCOUNT)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")