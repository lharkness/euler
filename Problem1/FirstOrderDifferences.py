
raw_numbers = []
differences = []

# 
# This code just generates the first-order differences for the "divided evenly by three or 5"
# Question, to see if a pattern emerges.
# It does: 2,1,3,1,2,3,3
#
for i in range(88):
    if (i % 3 == 0 or i % 5 == 0) and i != 0:
        raw_numbers.append(i)

for i in range(0, len(raw_numbers) - 2):
    differences.append(raw_numbers[i + 1] - raw_numbers[i])

print(raw_numbers)
print(differences)
