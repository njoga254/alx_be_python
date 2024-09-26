number = int(input("Enter a number to see its multiplication table: "))
#iterating from 1 to 10
for i in range(1, 11):
    product = number * i # product calculation
    #print multiplication table line
    print(f"{number} * {i} = {product}")