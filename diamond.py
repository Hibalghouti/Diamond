# Prompt the user to enter the number of rows
rows = int(input("Enter the number of rows: "))

# Generate the upper part of the diamond
for i in range(rows):
    # Print leading spaces
    print(' ' * (rows - i - 1), end='')
    # Print stars
    print('*' * (2 * i + 1))

# Generate the lower part of the diamond
for i in range(rows - 1):
    # Print leading spaces
    print(' ' * (i + 1), end='')
    # Print stars
    print('*' * (2 * (rows - i - 2) + 1))
