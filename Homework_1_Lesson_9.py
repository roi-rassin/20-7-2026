#Start

height = int(input("Enter height of pyramid: "))

for row in range(height):
    for col in range(1 + row):
        print("*", end=" ")
    print()

for row in range(height):
    for col in range(height - 1 - row):
        print("*", end=" ")
    print()

#Stop