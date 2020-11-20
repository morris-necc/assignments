groceries = ["banana", "apple", "orange"] #Because the question only asked for these 3 i had to add "pear" in the next line
groceries.append("pear")
stock = dict(zip(groceries, [6, 0, 32, 15]))
prices = dict(zip(groceries, [4, 2, 1.5, 3]))

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

print(compute_bill(groceries))