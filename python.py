
rows = int(input("Enter the number of rows: "))

#  upper part 
for i in range(0 ,rows ,1):
    print(' ' * (rows - i - 1),'')
    print('*' * (2 * i + 1)) #printing the stars

#  lower part
for i in range(0 ,rows - 1 ,1):
    print(' ' * (i + 1),'')
    print('*' * (2 * (rows - i - 1) + 1)) #printing the stars
