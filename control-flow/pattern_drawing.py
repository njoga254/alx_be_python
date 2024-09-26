size = int(input("Enter the size of the pattern: "))
#initialize the row counter
row = 0

#use a while loop to iterate through each row
while row < size:
    #use of for loop
    for col in range(size):
        print("*", end="")# print asteriks without advancing on a new line
    print() # print new character after the row
