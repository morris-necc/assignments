height = 0

while height % 2 == 0:
    height = int(input("Enter the height of the diamond(has to be odd):"))

for i in range(height):
    print(" " * (height - i - 1) + "*" * (i*2 + 1))

for i in range(height):
    print(" " * (i + 1) + "*" * ((height-i-1)*2-1))