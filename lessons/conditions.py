#                                  --CONDITIONS--



#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

age = input('Enter your age:')

# convert the string to int
your_age = int(age)

# determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# show the ticket price
print(f"You'll pay ${ticket_price} for the ticket")



#                                    --TERNARY OPERATOR--



#value_if_true if condition else value_if_false
age = input('Enter your age:')
ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is {ticket_price}")



# Python program to demonstrate nested ternary operator
a, b = 10, 20
 
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

#The pass statement is a statement that does nothing. It’s just a placeholder for the code that you’ll write in the future
counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    pass       