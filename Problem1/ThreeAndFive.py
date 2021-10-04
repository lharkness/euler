differences = [2,1,3,1,2,3,3]
number = 3
total = 0
index = -1
MAX_VALUE = 1000

#
#  Generate numbers from 3 to strictly less than MAX_VALUE
#  And add them to total
#  We generate the number by adding the next entry in our first order differences list
#
while number < MAX_VALUE:
    total = total + number
    index = (index + 1) % len(differences)
    number = number + differences[index]

print(total)