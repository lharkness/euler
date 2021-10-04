
##
# This is a recursive function that totals up the multiples of 3 or  5
# Strictly less than max
#
def three_or_five_recursive(num, total, max):
    if num >= max:
        return total
    elif num % 3 == 0 or num % 5 == 0 :
        return three_or_five_recursive(num + 1, total + num, max)
    else :
        return three_or_five_recursive(num + 1, total, max)

print(three_or_five_recursive(3, 0, 1000))

