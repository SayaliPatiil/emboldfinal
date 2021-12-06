"""Taking two numbers"""
num1 = 1.5
num2 = 6.3

""" Add two numbers """
addition = num1 + num2

"""Display the addition"""
print(f'The sum of {0} and {1} is {2}'.format(num1, num2, addition))
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

""" Add two numbers"""
addition = float(num1) + float(num2)

"""Display the sum"""
print(f'The sum of {0} and {1} is {2}'.format(num1, num2,addition))

# taking user input
ch = input("Enter a character: ")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is not an Alphabet")
