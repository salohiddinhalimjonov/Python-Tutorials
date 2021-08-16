#                                      --WHILE LOOPS--



max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1



command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")#Echo: quit
print(command)#quit
#If we change the values of variables inside conditions, loops the variable also changes outside the loops, conditions
        



#                                    --BREAK--



#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#result 
#1
#2
#3



#                                      --CONTINUE--



#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result
#result:
#1
#2
#4
#5
#6 


#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")




  basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit = input('Enter a fruit:')

index = 0
found_it = False

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item['fruit'] == fruit:
        found_it = True
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        break

    index += 1

if not found_it:
    qty = int(input(f'Enter the qty for {fruit}:'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)


