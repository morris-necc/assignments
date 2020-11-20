stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
} #There wasn't any stock information written in this question so I assumed we're using the one from Assignment 3

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for key in prices: #prints key along with its price and stock information
    print(key)
    print("price:", prices.get(key))
    print("stock:", stock[key])

total = 0
for key in prices: #calculates total and prints the expected revenue from every fruit
    print(prices.get(key)*stock[key])
    total += prices.get(key)*stock[key]

print(total)