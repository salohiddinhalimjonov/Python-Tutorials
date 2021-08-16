#                               --FOR LOOP--



for index in range(0, 11, 2):
    print(index)
#result
#0
#2
#4
#6
#8
#10

sum = 0
for num in range(101):
    sum += num

print(sum)#5050



#For else statement:




people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28},
        {'name': 'John', 'age': 26}]

name = input('Enter a name:')

found = False
for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break  #if we delete break the code gives all results if we write break it shows one result and code stops running 

if not found:
    print(f'{name} not found!')
     